from rest_framework import generics
from news.models import Event
from .serializers import EventSerializer, EventCreateSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventCreateSerializer
    model = Event
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = dict(serializer.data)

        # data['participants'] = User.objects.get(username=serializer.data['participants'])
        print(data)

        instance = Event.objects.create(
            **data
        )

        instance.participants.set(User.objects.get(username=serializer.data['participants']))

        return Response({'Success': True})
