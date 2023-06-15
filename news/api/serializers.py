from rest_framework import serializers
from news.models import Event
from django.contrib.auth.models import User
from django.utils import timezone


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'body', 'participants', 'file', 'publish', 'created', 'updated', 'event_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class EventCreateSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=True, max_length=250)
    # body = serializers.CharField(required=True, max_length=5000)
    participants = UserSerializer(many=True, read_only=True)
    # file = serializers.FileField(required=False, allow_empty_file=True, use_url="media/")
    # created = serializers.DateTimeField(required=True)
    # publish = serializers.DateTimeField(required=True)
    # event_date = serializers.DateTimeField(required=True)

    class Meta:
        model = Event
        fields = ('title', 'body', 'participants', 'publish', 'created', 'updated', 'event_date',)

