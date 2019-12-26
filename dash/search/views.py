from django.shortcuts import render
from panel.models import Province, School

def search(request):

    provinces = Province.objects.all().order_by('code')
    school_provinces = []
    province_number = 1

    total_school = School.objects.all().count()

    for p in provinces:
        school_province_count = School.objects.filter(province=p).count()
        school_provinces.append({
            'number': province_number,
            'province': p.name,
            'total': school_province_count,
        })
        province_number += 1

    context = {
        'region_list': school_provinces,
        'total_school': total_school,
    }

    return render(request, 'search/index.html', context)
