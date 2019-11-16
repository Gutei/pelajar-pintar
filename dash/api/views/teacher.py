from rest_framework import viewsets, status, parsers
from api.serializers import (SchoolSerializer, SchoolContactSerializer, TeacherSerializer, SchoolActivitySerializer,
                             SchoolExtracurricularSerializer, AllTeacherSerializer)
from panel.models import (School, SchoolContact, Teacher, SchoolActivity, SchoolExtracurricular)
from rest_framework.response import Response

from rest_framework.decorators import (api_view, authentication_classes,
                                       detail_route, list_route,
                                       parser_classes, permission_classes,
                                       renderer_classes)

# ViewSets define the view behavior.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = AllTeacherSerializer