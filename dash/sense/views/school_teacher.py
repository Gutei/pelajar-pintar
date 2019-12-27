from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.http import Http404, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from panel.services import format_number
from panel.models import School, Teacher, TeacherContact, AbstractSchool


class TeacherList(ListView):
    model = Teacher
    template_name = 'sense/lte/school-teacher/steach-view.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherList, self).get_context_data(**kwargs)
        abstract = AbstractSchool.objects.filter(user=self.request.user).first()
        school = School.objects.filter(school_number=abstract.school.school_number).first()
        context['Teachers'] = Teacher.objects.filter(school=school)
        return context


class TheacherCreate(CreateView):
    model = Teacher
    fields = ('name', 'address', 'photo',)
    template_name = 'sense/lte/school-teacher/steach-add.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TheacherCreate, self).get_context_data(*args, **kwargs)
        return context

    @transaction.atomic
    def form_valid(self, form):
        self.object = form.save(commit=False)
        abstract = AbstractSchool.objects.filter(user=self.request.user).first()
        school = School.objects.filter(school_number=abstract.school.school_number).first()
        self.object.school = school

        total_new_form = self.request.POST['new_detail_form']
        if int(total_new_form) > 0:
            tc = TeacherContact()
            for new_field in range(0, int(total_new_form)):
                tc.teacher = self.object
                tc.email = self.request.POST.get('email_new_{}'.format(new_field))
                tc.phone = format_number(self.request.POST.get('phone_new_{}'.format(new_field)))
            try:
                with transaction.atomic():
                    self.object.save()
                    tc.save()
            except Exception as e:
                context = {
                    'messages': 'Harap Minimal Isi Data *NAMA, *ALAMAT, *FOTO',
                    'tag': 'warning',
                    'subject': 'Terjadi Kesalahan'
                    }
                return render(self.request, self.template_name, context)
        return super(TheacherCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('steach_view')


class TeacherUpdate(UpdateView):
    model = Teacher
    fields = ('name', 'address', 'photo',)
    template_name = 'sense/lte/school-teacher/steach-add.html'
    context_object_name = "details"

    def get_context_data(self, *args, **kwargs):
        context = super(TeacherUpdate, self).get_context_data(*args, **kwargs)
        contact = TeacherContact.objects.filter(teacher=self.object)
        context['contacts'] = contact
        context['total_contact'] = contact.count()
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        '''
        Update or Delete Old Contact
        '''
        old_tc = TeacherContact.objects.filter(teacher=self.object)
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
                tc = TeacherContact()
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
                context = {
                    'messages': 'Harap Minimal Isi Data *NAMA, *ALAMAT, *FOTO',
                    'tag': 'warning',
                    'subject': 'Terjadi Kesalahan'
                    }
                return render(self.request, self.template_name, context)
        return super(TeacherUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('steach_view')


class TeacherDelete(DeleteView):
    model = Teacher
    success_url = reverse_lazy('steach_view')
    template_name = 'sense/lte/_includes/confirm_delete.html'
