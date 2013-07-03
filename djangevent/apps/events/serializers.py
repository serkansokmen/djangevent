from .models import Event
from rest_framework import serializers
from rest_framework import fields


# class SessionSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Session
#         fields = ('name')


# class LocationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Location
#         fields = ('address', 'city', 'province')


class EventSerializer(serializers.ModelSerializer):
    imageUrl = fields.CharField(source='get_image_url')

    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'location', 'imageUrl', 'sessions')
        depth = 2
        read_only_fields = ('id',)
