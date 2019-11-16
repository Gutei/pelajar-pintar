from django.contrib.auth.models import User
from rest_framework import serializers
from panel.models import StudentRegistration

# Serializers define the API representation.
class StudentRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentRegistration
        fields = '__all__'