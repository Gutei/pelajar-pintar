from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
import json
from django.http import JsonResponse
from panel.models import School, AbstractSchool, SchoolContact, Province, City


def getdetails(request):
    print("Pindh")
    if request.method == "GET":
        print("Jalan")
        # country_name = request.POST['country_name']
        country_name = request.GET['prov']
        print("ajax country_name ", country_name)

        result_set = []

        selected_country = Province.objects.get(name=country_name)
        print("selected country name ", selected_country)

        all_cities = City.objects.filter(province=selected_country).all()
        print(all_cities)

        for city in all_cities:
            print("city name", city.name)
            result_set.append({'name': city.name})

        return JsonResponse(
            json.dumps(result_set),
            mimetype='application/json',
            content_type='application/json',)


@transaction.atomic
def register(request):
    province = Province.objects.all()
    city = City.objects.all()

    type = School.TYPE
    level = School.LEVEL

    context = {
        'province': province,
        'city': city,
        'type': type,
        'level': level,
    }
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        new_user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password1),
        )
        new_user.is_active = True
        group = Group.objects.get(name='Schools')
        try:
            new_user.save()
            new_user.groups.add(group)
        except Exception as e:
            new_user.delete()
            print(e)
            return redirect(reverse('school-register'))

        prov = Province.objects.filter(id=request.POST.get('province')).first()
        cit = City.objects.filter(id=request.POST.get('city')).first()

        sch = School()

        if School.objects.filter(school_number=request.POST.get("school_number")):
            messages.success(request, 'Nomor Sekolah Sudah Terdaftar')
            return redirect(reverse('school-register'))
        else:
            sch.school_number = request.POST.get("school_number")

        sch.name = request.POST.get('name')
        sch.level = request.POST.get('level')
        sch.type = request.POST.get('type')
        sch.address = request.POST.get('address')
        sch.logo = request.POST.get('logo')
        sch.image = request.POST.get('image')
        sch.province = prov
        sch.city = cit

        try:
            sch.save()
        except Exception as e:
            new_user.delete()
            print(e)
            return redirect(reverse('school-register'))

        reg_1 = sch.id

        scho = School.objects.filter(id=reg_1).first()

        cont = SchoolContact()
        cont.school = scho
        cont.phone = request.POST.get('phone_contact')
        cont.email = request.POST.get('email_contact')

        try:
            cont.save()
        except Exception as e:
            sch.delete()
            new_user.delete()
            print(e)
            return redirect(reverse('school-register'))

        # reg_2 = new_user.save().id
        # usr = new_user.objects.filter(id=reg_2).first()

        abst = AbstractSchool()
        abst.user = new_user
        abst.school = scho

        try:
            abst.save()
        except Exception as e:
            new_user.delete()
            sch.delete()
            cont.delete()
            print(e)
            return render(request, 'schoreg/index.html', context)

    return render(request, 'schoreg/index.html', context)
