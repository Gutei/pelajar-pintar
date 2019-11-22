from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.db import transaction

def home(request):

    return render(request, 'seduh/index.html')