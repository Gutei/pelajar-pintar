from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.http import Http404, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from panel.services import format_number
from panel.models import School, AbstractSchool, SchoolContact


class SchoolProfil(UpdateView):
    model = School
    fields = ('name', 'address', 'type',)
    template_name = 'sense/lte/school-profil/sprof-add.html'
    context_object_name = "details"

    def get_object(self):
        abstract = AbstractSchool.objects.filter(user=self.request.user).first()
        return School.objects.get(pk=abstract.school.id)

    def get_context_data(self, *args, **kwargs):
        context = super(SchoolProfil, self).get_context_data(*args, **kwargs)
        abstract = AbstractSchool.objects.filter(user=self.request.user).first()
        school = School.objects.filter(school_number=abstract.school.school_number).first()
        contact = SchoolContact.objects.filter(school=school)
        context['contacts'] = contact
        context['total_contact'] = contact.count()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        abstract = AbstractSchool.objects.filter(user=self.request.user).first()
        school = School.objects.filter(school_number=abstract.school.school_number).first()
        '''
        Update or Delete Old Contact
        '''
        old_tc = SchoolContact.objects.filter(school=school)
        if old_tc.count() > 0:
            for old in old_tc:
                if self.request.POST.get('old-form-delete-{}'.format(old.id)):
                    old.delete()
                else:
                    old.email = self.request.POST.get('old-form-email-{}'.format(old.id))
                    old.phone = format_number(self.request.POST.get('old-form-phone-{}'.format(old.id)))
                    old.save()
        '''
        Create new contact 
        '''
        total_new_form = self.request.POST['new_detail_form']
        print(total_new_form)
        if int(total_new_form) > 0:
            for new_field in range(0, int(total_new_form)):
                tc = SchoolContact()
                tc.teacher = self.object
                tc.email = self.request.POST.get('email_new_{}'.format(new_field))
                tc.phone = format_number(self.request.POST.get('phone_new_{}'.format(new_field)))
                tc.save()
        '''
        Save teacher
        '''
        try:
            with transaction.atomic():
                self.object.save()
        except:
            return HttpResponseServerError()
        return super(SchoolProfil, self).form_valid(form)

    def get_success_url(self):
        return reverse('steach_view')
