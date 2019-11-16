from rest_framework import viewsets, status
from api.serializers import (ProvinceSerializer, CitySerializer)
from panel.models import (School, SchoolContact, Teacher, SchoolActivity, SchoolExtracurricular,
                          SchoolMagazine, SchoolMagazineActivity, Province, City)
from rest_framework.response import Response

from rest_framework.decorators import (api_view, authentication_classes,
                                       detail_route, list_route,
                                       parser_classes, permission_classes,
                                       renderer_classes, action)


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


    @detail_route(methods=['get'],)
    def get_cities(self, request, *args, **kwargs):
        province = Province.objects.get(id=kwargs.get('pk'))
        cities = City.objects.filter(province=province)

        page = self.paginate_queryset(cities)
        if page is not None:
            serializer = CitySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CitySerializer(cities, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)