from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
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
        try:
            with transaction.atomic():
                if form.is_valid():
                    try:
                        form.save()
                    except Exception as e:
                        messages.info(request, e)
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
                    form.delete()
                    messages.error(request, e)
                    return redirect(reverse('school-register'))

                reg_1 = sch.id

                scho = School.objects.filter(id=reg_1).first()

                cont = SchoolContact()
                cont.school = scho
                cont.phone = request.POST.get('phone')
                cont.email = request.POST.get('email')

                try:
                    cont.save()
                except Exception as e:
                    sch.delete()
                    form.delete()
                    messages.error(request, e)
                    return redirect(reverse('school-register'))

                reg_2 = form.save().pk
                usr = User.objects.filter(id=reg_2).first()

                abst = AbstractSchool()
                abst.user = usr
                abst.school = scho

                try:
                    abst.save()
                except Exception as e:
                    form.delete()
                    sch.delete()
                    cont.delete()
                    messages.error(request, e)

        except Exception as e:
            print(e)
            messages.error(request, 'Form submission Failed')
            return redirect(reverse('school-register'))

    return render(request, 'schoreg/clib/index.html', context)
