from django.shortcuts import render
from panel.models import School, StudentRegistration, City
from air.helper.unique_number_generator import get_uniqueid
from django.utils import timezone

# Create your views here.
def psb(request, pk):
    to_school = School.objects.filter(id=pk).first()
    gender = StudentRegistration.GENDERS
    faith = StudentRegistration.FAITHS

    city = City.objects.all()

    from_school = School.objects.all()
    message = ""

    context = {
        'from_school': from_school,
        'gender': gender,
        'faith': faith,
        'to_school': to_school,
        'city': city,
        'message': message,
    }

    if request.method == "POST":
        data = request.POST
        now = timezone.now()

        target_school = to_school
        domain_school = School.objects.filter(id=data['from_school']).first()
        registration_number = next(get_uniqueid())
        periode = "{}/{}".format(now.month,now.year)
        registration_year = now.year
        registration_month = now.month
        student_name = data['name']
        nisn = data['nisn']
        national_exam_number = data['national_exam_number']
        graduation_year = data['graduate_year']
        skhun_number = data['skhun']
        average_national_exam_scores = data['nem']
        parent_name = data['parent_name']
        mother_name = data['mother_name']
        number_of_siblings = data['siblings']
        student_gender = data['gender']
        birth_date = data['birth_date']
        birth_place = data['birth_place']
        student_faith = data['faith']
        student_phone = data['phone']
        student_email = data['email']
        parent_phone = data['parent_phone']

        if not request.FILES.get('student_photo'):
            context['message'] = 'Pas Foto Harus Di isi'
            return render(request, 'psb/index.html', context)

        if not request.FILES.get('skhun_photo'):
            context['message'] = 'Foto Ijazah/SKHUN Harus Di isi'
            return render(request, 'psb/index.html', context)

        psb = StudentRegistration(from_school=domain_school.name, to_school=target_school, registration_number=registration_number,
                                  periode=periode, registration_year=registration_year, registration_month=registration_month,
                                  student_name=student_name, nisn=nisn, national_exam_number=national_exam_number,
                                  graduation_year=graduation_year, skhun_number=skhun_number,
                                  average_national_exam_scores=average_national_exam_scores,
                                  parent_name=parent_name, mother_name=mother_name, number_of_siblings=number_of_siblings,
                                  gender=student_gender, birth_date=birth_date, birth_place=birth_place, faith=student_faith,
                                  student_phone=student_phone, parent_phone=parent_phone, email=student_email,
                                  image_student=request.FILES.get('student_photo'),
                                  image_skhun=request.FILES.get('skhun_photo'))
        try:
            psb.save()
        except Exception as e:
            context['message'] = e
            return render(request, 'psb/index.html', context)

        context['message'] = 'Success'

        return render(request, 'psb/index.html', context)

    return render(request, 'psb/index.html', context)