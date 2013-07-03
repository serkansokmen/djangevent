from .models import Event, Session, Location
from rest_framework import serializers
from rest_framework import fields


class SessionSerializer(serializers.ModelSerializer):
    creator = serializers.RelatedField(source='creator')
    level = serializers.RelatedField(source='level')
    voteCount = serializers.RelatedField(source='vote_count')

    class Meta:
        model = Session
        fields = (
            'name', 'creator', 'duration',
            'level', 'abstract', 'voteCount',)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('address', 'city', 'province')


class EventSerializer(serializers.ModelSerializer):

    sessions = SessionSerializer()
    location = LocationSerializer()
    imageUrl = fields.CharField(source='get_image_url')
    thumbUrl = fields.CharField(source='get_thumb_url')

    class Meta:
        model = Event
        fields = (
            'name', 'date', 'time', 'location',
            'imageUrl', 'thumbUrl', 'sessions')
