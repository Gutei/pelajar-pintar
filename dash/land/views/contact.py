from django.shortcuts import render
from panel.models import School, SchoolContact


# Create your views here.
def contact(request, *args, **kwargs):
    school = School.objects.filter(school_number='12251515').first()
    school_contact = SchoolContact.objects.filter(school__school_number='12251515').first()
    context = {
        'school': school,
        'contact': school_contact,
    }
    return render(request, 'land/listingo/contact.html', context)
