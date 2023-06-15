from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound

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


# class EventCreateView(generics.CreateAPIView):
#     serializer_class = EventCreateSerializer
#     model = Event
#     permission_classes = [AllowAny, ]
#
#     def post(self, request, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = dict(serializer.data)
#         print(data)
#         data['participants'] = User.objects.get(username=serializer.data['participants'])
#
#
#         event = Event.objects.create(**data)
#
        # for participant in participants:
        #     user = User.objects.get(username=participant.strip())
        #     event.participants.set(user)
        #
        # return Response({'Success': True})

@api_view(['POST'])
def create_event(request):
    serializer = EventCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    event = serializer.save()

    for participant_id in request.data.get('participants'):
        try:
            participant = User.objects.get(id=participant_id)
            event.participants.add(participant)
        except User.DoesNotExist:
            raise NotFound()

    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
