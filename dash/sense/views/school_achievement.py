from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.http import Http404, HttpResponseServerError
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from panel.models import School, SchoolAchievement


class AchievementList(ListView):
    model = SchoolAchievement
    template_name = 'sense/lte/school-achievement/sachiev-view.html'

    def get_context_data(self, **kwargs):
        context = super(AchievementList, self).get_context_data(**kwargs)
        school = School.objects.filter(school_number=1234567).first()
        context['Achievements'] = SchoolAchievement.objects.filter(school=school)
        return context


class AchievementCreate(CreateView):
    model = SchoolAchievement
    fields = ('name', 'description', 'image',)
    template_name = 'sense/lte/school-achievement/sachiev-add.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AchievementCreate, self).get_context_data(*args, **kwargs)
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

        return super(AchievementCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('sachiev_view')


class AchievementUpdate(UpdateView):
    model = SchoolAchievement
    fields = ['name', 'description', 'image']
    template_name = 'sense/lte/school-achievement/sachiev-add.html'
    context_object_name = "details"

    def get_context_data(self, *args, **kwargs):
        context = super(AchievementUpdate, self).get_context_data(*args, **kwargs)
        return context

    def form_valid(self, form):
        self.object.save()
        return super(AchievementUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('sachiev_view')


class AchievementDelete(DeleteView):
    model = SchoolAchievement
    success_url = reverse_lazy('sachiev_view')
    template_name = 'sense/lte/_includes/confirm_delete.html'
