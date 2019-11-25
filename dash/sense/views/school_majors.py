from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView

from panel.models import SchoolMajor


class SchoolMajorListView(ListView):
    model = SchoolMajor
    context_object_name = "all"

    template_name = 'sense/lte/school-majors/sm-view.html'

    def get_context_data(self, **kwargs):
        context = super(SchoolMajorListView, self).get_context_data(**kwargs)
        return context
