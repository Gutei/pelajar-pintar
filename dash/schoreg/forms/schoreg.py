from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from panel.models import School, SchoolContact, AbstractSchool
from django.contrib.admin import widgets
from django_select2.forms import Select2MultipleWidget, Select2Widget
from panel.models import Province, City


class UserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", ]


class SchoolForm(forms.ModelForm):
    school_number = forms.CharField(label="NPSN", widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    level = forms.ChoiceField(widget=Select2Widget(attrs={'class': 'form-control select2'}), choices=School.LEVEL)
    province = forms.ModelChoiceField(queryset=Province.objects.all(), widget=Select2Widget(attrs={'class': 'form-control select2'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=Select2Widget(attrs={'class': 'form-control select2'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    type = forms.ChoiceField(widget=Select2Widget(attrs={'class': 'form-control select2'}), choices=School.TYPE)

    class Meta:
        model = School
        fields = [
            "school_number", "name", "level", "province", "city",
            "address", "logo", "image", "type"
        ]

class SchoolForm(forms.ModelForm):
    school_number = forms.CharField(label="NPSN", widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    level = forms.ChoiceField(widget=Select2Widget(attrs={'class': 'form-control select2'}), choices=School.LEVEL)
    province = forms.ModelChoiceField(queryset=Province.objects.all(), widget=Select2Widget(attrs={'class': 'form-control select2'}))
    city = forms.ModelChoiceField(queryset=Province.objects.all(), widget=Select2Widget(attrs={'class': 'form-control select2'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    type = forms.ChoiceField(widget=Select2Widget(attrs={'class': 'form-control select2'}), choices=School.TYPE)

    class Meta:
        model = School
        fields = [
            "school_number", "name", "level", "province", "city",
            "address", "logo", "image", "type"
        ]


class ContactForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text'}))
    class Meta:
        model = SchoolContact
        fields = [
            "phone", "email"
        ]
