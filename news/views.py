from django.shortcuts import render
from datetime import date, timedelta
from .models import Event
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

        card = {
            'date': f"{day_name}, {card_date.day} {month_name}",
            'content': 'Совещание, УГМК',
            'is_current_day': card_date == current_date
        }
        week_cards.append(card)

    events = Event.objects.all()

    context = {
        'week_cards': week_cards,
        'events': events,
    }
    return render(request, 'news/main.html', context)


def get_news_page(request):
    return render(request, 'news/news.html')
