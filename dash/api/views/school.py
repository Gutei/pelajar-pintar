from rest_framework import viewsets, status
from api.serializers import (SchoolSerializer, SchoolContactSerializer, TeacherSerializer, SchoolActivitySerializer,
                             SchoolExtracurricularSerializer)
from panel.models import (School, SchoolContact, Teacher, SchoolActivity, SchoolExtracurricular)
from rest_framework.response import Response

from rest_framework.decorators import (api_view, authentication_classes,
                                       detail_route, list_route,
                                       parser_classes, permission_classes,
                                       renderer_classes)

# ViewSets define the view behavior.
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

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