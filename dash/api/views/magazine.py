from rest_framework import viewsets, status
from api.serializers import (SchoolSerializer, SchoolContactSerializer, TeacherSerializer, SchoolActivitySerializer,
                             SchoolExtracurricularSerializer, AllMagazineActivitySerializer, AllMagazineSerializer,
                             MagazineActivitySerializer)
from panel.models import (School, SchoolContact, Teacher, SchoolActivity, SchoolExtracurricular,
                          SchoolMagazine, SchoolMagazineActivity)
from rest_framework.response import Response

from rest_framework.decorators import (api_view, authentication_classes,
                                       detail_route, list_route,
                                       parser_classes, permission_classes,
                                       renderer_classes, action)


class MagazineViewSet(viewsets.ModelViewSet):
    queryset = SchoolMagazine.objects.all()
    serializer_class = AllMagazineSerializer


    @action(methods=['get'], detail=False)
    def get_all(self, request):
        magazines = SchoolMagazine.objects.all()

        page = self.paginate_queryset(magazines)
        if page is not None:
            serializer = AllMagazineSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AllMagazineSerializer(magazines, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)