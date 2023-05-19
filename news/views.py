from django.shortcuts import render
from datetime import date, timedelta
from .models import Event, News, Project, Work
import calendar


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
        event_titles = '\n '.join([event.title for event in events])

        card = {
            'date': f"{day_name}, {card_date.day} {month_name}",
            'content': event_titles if event_titles else '',
            'is_current_day': card_date == current_date
        }
        week_cards.append(card)

    today_events = Event.objects.filter(event_date__date=current_date)

    context = {
        'week_cards': week_cards,
        'today_events': today_events,
    }
    return render(request, 'news/main.html', context)


def get_events_by_date(request, year, month, day):
    selected_date = date(year, month, day)
    events = Event.objects.filter(event_date__date=selected_date)

    context = {
        'selected_date': selected_date,
        'events': events,
    }
    return render(request, 'news/events.html', context)


def get_news_page(request):
    news = News.objects.all()

    context = {
        'news': news
    }
    return render(request, 'news/news.html', context)
