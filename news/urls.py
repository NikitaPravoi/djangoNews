from django.urls import path
from . import views

app_name = 'djangoNews'
urlpatterns = [
    path('', views.get_week_cards, name='main'),
    path('news/', views.get_news_page, name='news')
]