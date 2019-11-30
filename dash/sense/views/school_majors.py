from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.http import Http404, HttpResponseServerError
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from panel.models import School, SchoolMajor


class MajorList(ListView):
    model = SchoolMajor
    template_name = 'sense/lte/school-majors/sm-view.html'

    def get_context_data(self, **kwargs):
        context = super(MajorList, self).get_context_data(**kwargs)
        school = School.objects.filter(school_number=1234567).first()
        context['majors'] = SchoolMajor.objects.filter(school=school)
        return context


class MajorCreate(CreateView):
    model = SchoolMajor
    fields = ('name', 'image')
    template_name = 'sense/lte/school-majors/sm-add.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MajorCreate, self).get_context_data(*args, **kwargs)
        # data['group'] = MsUser.objects.filter(user=self.request.user).first()
        return context

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.school = School.objects.filter(school_number=1234567).first()
        try:
            with transaction.atomic():
                self.object.save()
        except:
            return HttpResponseServerError()

        return super(MajorCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('sm_view')


class MajorUpdate(UpdateView):
    model = SchoolMajor
    fields = ['name', 'image']
    template_name = 'sense/lte/school-majors/sm-add.html'
    context_object_name = "details"

    def get_context_data(self, *args, **kwargs):
        context = super(MajorUpdate, self).get_context_data(*args, **kwargs)
        return context

    def form_valid(self, form):
        self.object.save()
        return super(MajorUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('sm_view')


class MajorDelete(DeleteView):
    model = SchoolMajor
    success_url = reverse_lazy('sm_view')
    template_name = 'sense/lte/_includes/confirm_delete.html'

# class MajorDelete(DeleteView):
#     def get_object(self, queryset=None):
#         """ Hook to ensure object is owned by request.user. """
#         obj = super(MajorDelete, self).get_object()
#         if not obj.owner == self.request.user:
#             raise Http404
#         return obj
