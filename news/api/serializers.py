from rest_framework import serializers
from news.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'body', 'participants', 'file', 'publish', 'created', 'updated', 'event_date']


class EventCreateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=250)
    body = serializers.CharField(required=True, max_length=5000)
    participants = serializers.CharField(required=False)
    file = serializers.FileField(required=False)
    publish = serializers.DateTimeField(required=True)
    created = serializers.DateTimeField(required=True)
    event_date = serializers.DateTimeField(required=True)

    def validate(self, data):
        return data

    def create(self, instance, validated_data):
        validated_data(instance.data)
        return instance
