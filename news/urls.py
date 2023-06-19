from django.urls import path
from . import views

app_name = 'djangoNews'
urlpatterns = [
    path('', views.get_week_cards, name='main'),
    path('news/', views.get_news_page, name='news'),
    path('events/<int:year>/<int:month>/<int:day>/', views.get_events_by_date, name='events-by-date'),
    path('calendar/', views.render_calendar, name='calendar'),
    path('create/event/', views.render_form, name='form'),
    path('success/', views.event_post_form, name='post_form'),
    path('gantt/', views.render_gantt, name='gantt'),
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
]
