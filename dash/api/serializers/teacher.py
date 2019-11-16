from django.contrib.auth.models import User
from rest_framework import serializers
from panel.models import Teacher, TeacherContact
from api.serializers import SchoolSerializer


# Serializers define the API representation.

class TeacherMinimalizeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherContact
        fields = ('id', 'phone', 'email')

class TeacherSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()

    def get_contacts(self, obj):
        contacts = TeacherContact.objects.filter(teacher=obj)
        serializer = TeacherMinimalizeContactSerializer(contacts, many=True)
        return serializer.data

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'address', 'photo', 'contacts')

class AllTeacherSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    contacts = serializers.SerializerMethodField()

    def get_contacts(self, obj):
        contacts = TeacherContact.objects.filter(teacher=obj)
        serializer = TeacherMinimalizeContactSerializer(contacts, many=True)
        return serializer.data

    class Meta:
        model = Teacher
        fields = ('id', 'school', 'name', 'address', 'photo', 'contacts')


class TeacherContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'techer', 'phone', 'email')