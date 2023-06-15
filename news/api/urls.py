from django.urls import path
from . import views
from .views import create_event

app_name = 'djangoNews'

urlpatterns = [
    path('events/', views.EventListView.as_view(),
         name='event_list'),
    path('events/<pk>/',
         views.EventDetailView.as_view(),
         name='event_detail'),
    path('create/',
         create_event,
         name='event_create'),
]
