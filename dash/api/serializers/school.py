from django.contrib.auth.models import User
from rest_framework import serializers
from panel.models import School, SchoolContact, SchoolActivity, SchoolExtracurricular, Province, City, SchoolMajor

# Serializers define the API representation.

class SchoolProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ('id', 'code', 'name')

class SchoolMajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolMajor
        fields = ('name', 'image')

class SchoolCitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'code', 'name')

class SchoolContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolContact
        fields = ('id', 'phone', 'email')


class SchoolSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()
    province = SchoolProvinceSerializer()
    city = SchoolCitySerializer()
    major = serializers.SerializerMethodField()

    def get_contacts(self, obj):
        contacts = SchoolContact.objects.filter(school=obj)
        serializer = SchoolContactSerializer(contacts, many=True)
        return serializer.data

    def get_major(self, obj):
        major = SchoolMajor.objects.filter(school=obj)
        serializer = SchoolMajorSerializer(major, many=True)
        return serializer.data

    class Meta:
        model = School
        fields = '__all__'


class SchoolActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolActivity
        fields = ('id', 'title', 'description', 'image', 'created', 'updated')


class SchoolExtracurricularSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolExtracurricular
        fields = ('id', 'name', 'description', 'image', 'created', 'updated')