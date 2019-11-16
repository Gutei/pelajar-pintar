from rest_framework import serializers
from panel.models import Province, City
from api.serializers import SchoolSerializer, SchoolActivitySerializer


# Serializers define the API representation.

class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ('id', 'code', 'name')


class CitySerializer(serializers.ModelSerializer):

    province = ProvinceSerializer()

    class Meta:
        model = City
        fields = ('id', 'province', 'code', 'name')