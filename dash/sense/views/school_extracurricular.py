from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.http import Http404, HttpResponseServerError
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from panel.models import School, SchoolExtracurricular, AbstractSchool


class ExtracurricularList(ListView):
    model = SchoolExtracurricular
    template_name = 'sense/lte/school-extracurricular/sex-view.html'

    def get_context_data(self, **kwargs):
        context = super(ExtracurricularList, self).get_context_data(**kwargs)
        abstract = AbstractSchool.objects.filter(user=self.request.user).first()
        school = School.objects.filter(school_number=abstract.school.school_number).first()
        context['extras'] = SchoolExtracurricular.objects.filter(school=school)
        return context


class ExtracurricularCreate(CreateView):
    model = SchoolExtracurricular
    fields = ('name', 'description', 'image',)
    template_name = 'sense/lte/school-extracurricular/sex-add.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ExtracurricularCreate, self).get_context_data(*args, **kwargs)
        return context

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save(commit=False)
        abstract = AbstractSchool.objects.filter(user=self.request.user).first()
        school = School.objects.filter(school_number=abstract.school.school_number).first()
        self.object.school = school
        try:
            with transaction.atomic():
                self.object.save()
        except:
            return HttpResponseServerError()

        return super(ExtracurricularCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('sex_view')


class ExtracurricularUpdate(UpdateView):
    model = SchoolExtracurricular
    fields = ['name', 'description', 'image']
    template_name = 'sense/lte/school-extracurricular/sex-add.html'
    context_object_name = "details"

    def get_context_data(self, *args, **kwargs):
        context = super(ExtracurricularUpdate, self).get_context_data(*args, **kwargs)
        return context

    def form_valid(self, form):
        self.object.save()
        return super(ExtracurricularUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('sex_view')


class ExtracurricularDelete(DeleteView):
    model = SchoolExtracurricular
    success_url = reverse_lazy('sex_view')
    template_name = 'sense/lte/_includes/confirm_delete.html'
