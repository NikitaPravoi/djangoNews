from django.shortcuts import render
from datetime import date, timedelta
from rest_framework import generics
from rest_framework.response import Response
from .api.serializers import RegisterSerializer, UserSerializer
from .models import Event, News, Project, Work
import calendar
from django.http import JsonResponse
# from django.contrib.auth import authenticate, login


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_week_cards(request):
    current_date = date.today()
    monday = current_date - timedelta(days=current_date.weekday())  # Находим понедельник текущей недели

    week_cards = []

    # Создаем карточки на каждый день недели
    for i in range(7):
        card_date = monday + timedelta(days=i)

        day_name = calendar.day_name[card_date.weekday()].capitalize()

        month_name = calendar.month_name[card_date.month]

        events = Event.objects.filter(event_date__date=card_date)
        year = card_date.year.real
        month = card_date.month.real
        day = card_date.day.real

        event_titles = [event.title for event in events]

        card = {
            'date': f"{day_name}, {card_date.day} {month_name}",
            'link_date': {'year': year, 'month': month, 'day': day},
            # 'content': event_titles if event_titles else '',
            'contents': event_titles if event_titles else ['Нет событий', ],
            'is_current_day': card_date == current_date
        }
        week_cards.append(card)

    context = {
        'week_cards': week_cards,
    }
    return render(request, 'news/main.html', context)


def get_events_by_date(request, year, month, day):
    selected_date = date(year, month, day)
    events = Event.objects.filter(event_date__date=selected_date)

    current_date = date.today()
    monday = current_date - timedelta(days=current_date.weekday())  # Находим понедельник текущей недели

    week_cards = []

    # Создаем карточки на каждый день недели
    for i in range(7):
        card_date = monday + timedelta(days=i)

        day_name = calendar.day_name[card_date.weekday()].capitalize()

        month_name = calendar.month_name[card_date.month]

        events = Event.objects.filter(event_date__date=card_date)
        year = card_date.year.real
        month = card_date.month.real
        day = card_date.day.real

        event_titles = [event.title for event in events]

        card = {
            'date': f"{day_name}, {card_date.day} {month_name}",
            'link_date': {'year': year, 'month': month, 'day': day},
            # 'content': event_titles if event_titles else '',
            'contents': event_titles if event_titles else ['Нет событий', ],
            'is_current_day': card_date == current_date
        }
        week_cards.append(card)

    today_events = Event.objects.filter(event_date__date=selected_date)

    context = {
        'week_cards': week_cards,
        'today_events': today_events,
    }
    return render(request, 'news/main.html', context)


def get_news_page(request):
    news = News.objects.all()

    context = {
        'news': news
    }
    return render(request, 'news/news.html', context)


def render_calendar(request):

    events = Event.objects.all()

    works = Work.objects.all()

    context = {
        'events': events,
        'works': works
    }
    return render(request, 'news/calendar.html', context)


def render_form(request):

    # print(request.method)
    # print(request.POST)
    return render(request, 'news/forms/event_creation.html')


def render_gantt(request):

    # print(request.method)
    # print(request.POST)
    return render(request, 'news/gantt.html')


def event_post_form(request):
    if is_ajax(request):
        try:
            # field = request.POST['принимаемое поле']
            # field2 = request.POST['принимаемое поле']
            # field3 = request.POST['принимаемое поле']
            # field4 = request.POST['принимаемое поле']
            #
            # data_modal_window = Event.objects.created(id=id)
            # data_modal_window.save()
            print(request.POST)
            return JsonResponse({'update': True, 'id': id}, status=200)
        except ValueError as ex:
            print(ex)


def signin_view(request):
    return render(request, 'news/auth/signin.html')


def signup_view(request):
    return render(request, 'news/auth/signup.html')