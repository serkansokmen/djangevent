from .models import Event, Session, Location
from rest_framework import serializers
from rest_framework import fields


class SessionSerializer(serializers.ModelSerializer):
    creator = serializers.RelatedField(source='creator')
    voteCount = serializers.RelatedField(source='vote_count')
    level = serializers.RelatedField(source='get_level_display')
    duration = serializers.RelatedField(source='get_duration_display')

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
    image = serializers.ImageField(source='image')
    imageUrl = fields.CharField(source='get_image_url', required=False)
    thumbUrl = fields.CharField(source='get_thumb_url', required=False)

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'date', 'time',
            'location',
            'image', 'imageUrl', 'thumbUrl',
            'sessions')
