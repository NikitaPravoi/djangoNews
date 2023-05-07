from django.urls import path
from . import views

app_name = 'djangoNews'
urlpatterns = [
    path('', views.get_html, name='news'),
]