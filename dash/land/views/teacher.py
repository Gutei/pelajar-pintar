from django.shortcuts import render
from panel.models import Teacher

from django.core.paginator import Paginator


def teacher(request):
    teacher_list = Teacher.objects.filter(school__school_number='12251515')
    paginator = Paginator(teacher_list, 8)  # Show 25 contacts per page

    page = request.GET.get('page')
    teachers = paginator.get_page(page)
    return render(request, 'land/listingo/teacher.html', {'teachers': teachers})
