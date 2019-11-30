from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


def school_sense(request):
    return render(request, 'sense/lte/school_sense/school_sense.html')
