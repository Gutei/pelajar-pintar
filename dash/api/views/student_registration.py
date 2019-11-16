from rest_framework import viewsets, status, parsers, permissions, authentication
from api.serializers import (SchoolSerializer, SchoolContactSerializer, TeacherSerializer, SchoolActivitySerializer,
                             SchoolExtracurricularSerializer, AllTeacherSerializer, StudentRegistrationSerializer)
from panel.models import (School, SchoolContact, Teacher, SchoolActivity, SchoolExtracurricular, StudentRegistration)
from rest_framework.response import Response

from rest_framework.decorators import (api_view, authentication_classes,
                                       detail_route, list_route,
                                       parser_classes, permission_classes,
                                       renderer_classes, action)

# ViewSets define the view behavior.
class StudentRegistrationViewSet(viewsets.ModelViewSet):
    queryset = StudentRegistration.objects.all()
    serializer_class = StudentRegistrationSerializer
    parser_classes = [parsers.MultiPartParser]

    @action(permission_classes=(permissions.AllowAny,), detail=False, methods=['post',])
    def registration(self, request):

        if not request.META.get('HTTP_X_TOKEN'):
            return Response({'message': 'Not acceptable header request'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        data = request.data

        from_school = data.get('from_school')
        to_school = data.get('to_school')
        registration_number = data.get('registration_number')
        periode = data.get('periode')
        registration_year = data.get('registration_year')
        registration_month = data.get('registration_month')
        student_name = data.get('student_name')
        nisn = data.get('nisn')
        national_exam_number = data.get('national_exam_number')
        graduation_year = data.get('graduation_year')
        skhun_number = data.get('skhun_number')
        average_national_exam_scores = data.get('average_national_exam_scores')
        parent_name = data.get('parent_name')
        mother_name = data.get('mother_name')
        number_of_siblings = data.get('number_of_siblings')
        gender = data.get('gender')
        birth_date = data.get('birth_date')
        birth_place = data.get('birth_place')
        faith = data.get('faith')
        student_phone = data.get('student_phone')
        parent_phone = data.get('parent_phone')
        email = data.get('email')
        image_student = data.get('image_student')
        image_skhun = data.get('image_skhun')

        registration = StudentRegistration(from_school=from_school,
                                           to_school=to_school,
                                           registration_number=registration_number,
                                           periode=periode,
                                           registration_year=registration_year,
                                           registration_month=registration_month,
                                           student_name=student_name,
                                           nisn=nisn,
                                           national_exam_number=national_exam_number,
                                           graduation_year=graduation_year,
                                           skhun_number=skhun_number,
                                           average_national_exam_scores=average_national_exam_scores,
                                           parent_name=parent_name,
                                           mother_name=mother_name,
                                           number_of_siblings=number_of_siblings,
                                           gender=gender,
                                           birth_date=birth_date,
                                           birth_place=birth_place,
                                           faith=faith,
                                           student_phone=student_phone,
                                           parent_phone=parent_phone,
                                           email=email,
                                           image_student=image_student,
                                           image_skhun=image_skhun
                                           )

        try:
            registration.save()
        except:
            return Response({'message': 'Failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({}, status=status.HTTP_200_OK)