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
        fields = ('id', 'last_name', 'first_name', 'username', 'email')


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


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            last_name=validated_data['first_name'],
            first_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
