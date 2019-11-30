from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


def register(request):
    return render(request, 'sense/lte/sense/sense.html')
