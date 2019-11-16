from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from panel.models import School


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", ]


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ["school_number", "name", "level", "address", "logo", "image"]
