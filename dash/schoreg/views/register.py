from django.shortcuts import render, redirect
from django.contrib import messages
from schoreg.forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
    else:
        form = RegisterForm()

    return render(request, "schoreg/register.html", {"form": form})
