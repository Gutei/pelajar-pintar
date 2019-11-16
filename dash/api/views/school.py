import json
from rest_framework import viewsets, status
from api.serializers import (SchoolSerializer, SchoolContactSerializer, TeacherSerializer, SchoolActivitySerializer,
                             SchoolExtracurricularSerializer)
from panel.models import (School, SchoolContact, Teacher, SchoolActivity, SchoolExtracurricular, Province, City)
from rest_framework.response import Response

from rest_framework.decorators import (api_view, authentication_classes,
                                       detail_route, list_route,
                                       parser_classes, permission_classes,
                                       renderer_classes)

# ViewSets define the view behavior.
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @list_route(methods=['get', ])
    def area(self, request):

        if not request.query_params.get('city'):
            if not request.query_params.get('province'):
                school = School.objects.all()
            else:
                province = Province.objects.filter(code=request.query_params.get('province')).first()
                school = School.objects.filter(province=province)
        else:
            city = City.objects.filter(code=request.query_params.get('city')).first()
            school = School.objects.filter(city=city)

        page = self.paginate_queryset(school)
        if page is not None:
            serializer = SchoolSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SchoolSerializer(school, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @detail_route(methods=['get', ])
    def get_contacts(self, request, *args, **kwargs):

        contacts = SchoolContact.objects.filter(school=kwargs.get('pk'))

        serializer = SchoolContactSerializer(contacts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @detail_route(methods=['get', ])
    def get_school_teachers(self, request, *args, **kwargs):

        teachers = Teacher.objects.filter(school=kwargs.get('pk'))

        page = self.paginate_queryset(teachers)
        if page is not None:
            serializer = TeacherSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = TeacherSerializer(teachers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @detail_route(methods=['get', ])
    def get_school_activities(self, request, *args, **kwargs):
        activities = SchoolActivity.objects.filter(school=kwargs.get('pk'))

        page = self.paginate_queryset(activities)
        if page is not None:
            serializer = SchoolActivitySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SchoolActivitySerializer(activities, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @detail_route(methods=['get', ])
    def get_school_extra(self, request, *args, **kwargs):
        extracurricular = SchoolExtracurricular.objects.filter(school=kwargs.get('pk'))

        page = self.paginate_queryset(extracurricular)
        if page is not None:
            serializer = SchoolExtracurricularSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = SchoolExtracurricularSerializer(extracurricular, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @detail_route(methods=['post', ])
    def add_teacher(self, request, *args, **kwargs):
        school = School.objects.get(id=kwargs.get('pk'))

        if not request.data.get('name'):
            return Response({'message': 'name can not be null'}, status=status.HTTP_400_BAD_REQUEST)

        if not request.data.get('address'):
            address = ""
        else:
            address = request.data.get('address')

        teacher = Teacher(
            school=school,
            name=request.data.get('name'),
            address=address
        )

        teacher.save()

        serializer = TeacherSerializer(teacher, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @list_route(methods=['get', ])
    def get_const(self, request, *args, **kwargs):
        data = {
            'levels': {
                'TK': 0,
                'PAUD': 1,
                'SD': 2,
                'MI': 3,
                'SMP': 4,
                'MTS': 5,
                'SMA': 6,
                'SMK': 7,
                'MA': 8,
            },
            'types': {
                'NEGERI':0,
                'SWASTA':1
            },
        }

        return Response(data, status=status.HTTP_200_OK)