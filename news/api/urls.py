from django.urls import path
from . import views

app_name = 'djangoNews'

urlpatterns = [
    path('events/', views.EventListView.as_view(),
         name='event_list'),
    path('events/<pk>/',
         views.EventDetailView.as_view(),
         name='event_detail'),
    path('create/',
         views.EventCreateView.as_view(),
         name='event_create'),
]
