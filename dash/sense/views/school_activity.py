from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.http import Http404, HttpResponseServerError
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from panel.models import School, SchoolActivity


class ActivityList(ListView):
    model = SchoolActivity
    template_name = 'sense/lte/school-activity/sac-view.html'

    def get_context_data(self, **kwargs):
        context = super(ActivityList, self).get_context_data(**kwargs)
        school = School.objects.filter(school_number=1234567).first()
        context['Activitys'] = SchoolActivity.objects.filter(school=school)
        return context


class ActivityCreate(CreateView):
    model = SchoolActivity
    fields = ('title', 'description', 'image',)
    template_name = 'sense/lte/school-activity/sac-add.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ActivityCreate, self).get_context_data(*args, **kwargs)
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

        return super(ActivityCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('sac_view')


class ActivityUpdate(UpdateView):
    model = SchoolActivity
    fields = ['title', 'description', 'image']
    template_name = 'sense/lte/school-activity/sac-add.html'
    context_object_name = "details"

    def get_context_data(self, *args, **kwargs):
        context = super(ActivityUpdate, self).get_context_data(*args, **kwargs)
        return context

    def form_valid(self, form):
        self.object.save()
        return super(ActivityUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('sac_view')


class ActivityDelete(DeleteView):
    model = SchoolActivity
    success_url = reverse_lazy('sac_view')
    template_name = 'sense/lte/_includes/confirm_delete.html'
