from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.db import transaction
from schoreg.forms import UserForm, SchoolForm, ContactForm
from panel.models import School, AbstractSchool, SchoolContact, Province, City


def register(request):

    province = Province.objects.all()
    city = City.objects.all()

    type = School.TYPE
    level = School.LEVEL

    context = {
        'province': province,
        'city': city,
        'type': type,
        'level': level,
        'user_form': UserForm,
    }
    return render(request, 'schoreg/clib/index.html', context)
