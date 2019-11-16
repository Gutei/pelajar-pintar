from rest_framework import serializers
from panel.models import SchoolMagazine, SchoolMagazineActivity, SchoolActivity
from api.serializers import SchoolSerializer, SchoolActivitySerializer


# Serializers define the API representation.

class MagazineActivitySerializer(serializers.ModelSerializer):

    activity = SchoolActivitySerializer()

    class Meta:
        model = SchoolMagazineActivity
        fields = ('id', 'activity')

class AllMagazineSerializer(serializers.ModelSerializer):

    school = SchoolSerializer()
    activities = serializers.SerializerMethodField()

    def get_activities(self, obj):
        activities = SchoolMagazineActivity.objects.filter(magazine=obj)
        serializer = MagazineActivitySerializer(activities, many=True)
        return serializer.data


    class Meta:
        model = SchoolMagazine
        fields = '__all__'


class AllMagazineActivitySerializer(serializers.ModelSerializer):

    magazine = AllMagazineSerializer()
    activity = SchoolActivitySerializer

    class Meta:
        model = SchoolMagazineActivity
        field = '__all__'

class SchoolMagazineSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolMagazine
        fields = ('id', 'title', 'published_date', 'is_published')