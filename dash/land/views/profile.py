from django.shortcuts import render
from panel.models import School

# Create your views here.
def profile(request, *args, **kwargs):
    school = School.objects.all()
    context = {
        'school': school,
    }

    return render(request, 'land/index.html', context)