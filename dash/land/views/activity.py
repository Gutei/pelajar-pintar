from django.shortcuts import render
from panel.models import School, SchoolActivity
from django.core.paginator import Paginator


def activity(request):
    activity_list = SchoolActivity.objects.filter(school__school_number='12251515').order_by('-date')
    paginator = Paginator(activity_list, 6)  # Show 25 contacts per page

    page = request.GET.get('page')
    activs = paginator.get_page(page)
    return render(request, 'land/listingo/activity.html', {'activity': activs})


def activity_view(request, id):
    details = SchoolActivity.objects.filter(school__school_number='12251515', id=id).first()
    context = {
        'details': details,
    }
    return render(request, 'land/listingo/details.html', context)
