from django.shortcuts import render
from django.core.paginator import Paginator
from panel.models import School, SchoolMajor, SchoolAchievement, SchoolActivity

# # Create your views here.
# def profile(request, *args, **kwargs):
#     school = School.objects.all()
#     context = {
#         'school': school,
#     }
#     return render(request, 'land/listingo/home.html', context)


def profile(request):
    major_list = SchoolMajor.objects.filter(school__school_number='12251515')
    achiev_list = SchoolAchievement.objects.filter(school__school_number='12251515').order_by('-created')
    activity_list = SchoolActivity.objects.filter(school__school_number='12251515').order_by('-date')

    # paginator = Paginator(major_list, 8)  # Show 25 contacts per page
    #
    # page = request.GET.get('page')
    # majors = paginator.get_page(page)
    achiev = Paginator(achiev_list, 6).get_page(1)
    activity = Paginator(activity_list, 6).get_page(1)

    context = {
        'majors': major_list,
        'achievs': achiev,
        'activity': activity,
    }
    return render(request, 'land/listingo/home.html', context)
