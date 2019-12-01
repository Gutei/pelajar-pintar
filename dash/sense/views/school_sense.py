from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def school_sense(request):
    context = {
        'user': request.user,
    }
    return render(request, 'sense/lte/school_sense/school_sense.html', context)
