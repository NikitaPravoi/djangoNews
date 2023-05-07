from django.shortcuts import render
# Create your views here.


def get_html(request):
    return render(request, 'news/card.html')
