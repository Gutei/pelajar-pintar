from django.contrib.auth.models import User
from rest_framework import serializers
from panel.models import School, SchoolContact, SchoolActivity, SchoolExtracurricular

# Serializers define the API representation.
class SchoolContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolContact
        fields = ('id', 'phone', 'email')


class SchoolSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()

    def get_contacts(self, obj):
        contacts = SchoolContact.objects.filter(school=obj)
        serializer = SchoolContactSerializer(contacts, many=True)
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