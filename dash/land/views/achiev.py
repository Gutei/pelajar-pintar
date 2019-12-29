from django.shortcuts import render
from panel.models import School, SchoolAchievement
from django.core.paginator import Paginator


def achiev(request):
    achiev_list = SchoolAchievement.objects.filter(school__school_number='12251515').order_by('-created')
    paginator = Paginator(achiev_list, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    achievs = paginator.get_page(page)
    return render(request, 'land/listingo/achiev.html', {'achievment': achievs})


def achiev_view(request, id):
    details = SchoolAchievement.objects.filter(school__school_number='12251515', id=id).first()
    context = {
        'details': details,
    }
    return render(request, 'land/listingo/details.html', context)
