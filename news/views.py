from django.shortcuts import render, redirect
from datetime import date, timedelta
from .models import Event, News, Project, Work, Message
import calendar
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.dateparse import parse_datetime


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
    # print(request.user.is_authenticated)
    context = {
        'week_cards': week_cards,
        'current_date': current_date,
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
        'current_date': current_date,
    }
    return render(request, 'news/main.html', context)


def get_news_page(request):
    news = News.objects.all()

    messages = Message.objects.all()

    context = {
        'news': news,
        'messages': messages,
    }
    return render(request, 'news/news.html', context)


def render_calendar(request):

    events = Event.objects.all()

    works = Work.objects.all()

    context = {
        'events': events,
        'works': works,
    }
    return render(request, 'news/calendar.html', context)


def render_form(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'news/forms/event_creation.html', context)


def render_gantt(request):
    return render(request, 'news/gantt.html')


def event_post_form(request):
    if is_ajax(request):
        try:
            request_data = dict(request.POST)
            print(request_data)
            title = request_data['key1'][0]
            body = request_data['key2'][0]
            participants_usernames = request_data['key3[]']
            published = parse_datetime(*request_data['key5'])
            event_date = parse_datetime(*request_data['key6'])
            print(title, body, participants_usernames, published, event_date)

            participants = User.objects.filter(username__in=participants_usernames)

            event = Event(title=title, body=body, publish=published, event_date=event_date)
            event.save()
            event.participants.set(participants)

            message = Message(theme=f'Создано событие "{title}"!',
                              text=f'Описание события: "{body}". \n Дата события: {event_date}',
                              date_message=published)
            message.save()

            return JsonResponse({'update': 'true'})
        except Exception as ex:
            print(ex)


def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('log')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            message = 'Неправильное имя пользователя или пароль'
    else:
        message = ''
    return render(request, 'news/auth/signin.html', {'message': message})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        _first_name = request.POST.get('first_name')
        _last_name = request.POST.get('last_name')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = _first_name
        user.last_name = _last_name
        user.save()

        return redirect('/signin/')
    else:
        message = ''
    return render(request, 'news/auth/signup.html', {'message': message})


def logout_view(request):
    logout(request)
    return redirect('/signin/')
