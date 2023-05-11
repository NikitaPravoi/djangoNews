from django.shortcuts import render
from datetime import date, timedelta
import calendar


def get_week_cards(request):
    current_date = date.today()
    week_cards = []

    # Создаем карточки на каждый день недели вперед
    for i in range(7):
        card_date = current_date + timedelta(days=i)
        day_name = calendar.day_name[card_date.weekday()].capitalize()
        month_name = calendar.month_name[card_date.month]

        card = {
            'date': f"{day_name}, {card_date.day} {month_name}",
            'content': 'Совещание, УГМК'  # Здесь может быть ваше содержимое карточки
        }
        week_cards.append(card)

    context = {
        'week_cards': week_cards
    }
    return render(request, 'news/base.html', context)
