from django.shortcuts import render
from panel.models import School

# Create your views here.
def extracurriculer(request, *args, **kwargs):
    school = School.objects.all()
    context = {
        'school': school,
    }

    return render(request, 'land/listingo/extracurr.html', context)