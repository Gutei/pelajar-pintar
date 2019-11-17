from django.shortcuts import render
from django.contrib import messages
from django.db import transaction
from schoreg.forms import UserForm
from django.contrib.auth.models import User
from panel.models import School, AbstractSchool, SchoolContact, Province, City


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
        'user_form': UserForm,
    }
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                    messages.success(request, 'Form submission successful')
            except Exception as e:
                messages.error(request, e)

        prov = Province.objects.filter(id=request.POST.get('province')).first()
        cit = City.objects.filter(id=request.POST.get('city')).first()

        sch = School()
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
            with transaction.atomic():
                sch.save()
        except Exception as e:
            messages.error(request, e)

        reg_1 = sch.pk

        scho = Province.objects.filter(id=reg_1).first()

        cont = SchoolContact()
        cont.school = scho
        cont.phone = request.POST.get('phone')
        cont.email = request.POST.get('email')

        try:
            with transaction.atomic():
                cont.save()
        except Exception as e:
            messages.error(request, e)

        reg_2 = form.save().pk
        usr = User.objects.filter(id=reg_2).first()

        abst = AbstractSchool()
        abst.user = usr
        abst.school = scho

        try:
            with transaction.atomic():
                abst.save()
        except Exception as e:
            messages.error(request, e)

    else:
        messages.error(request, 'Form submission Failed')

    return render(request, 'schoreg/clib/index.html', context)
