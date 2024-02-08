from importlib.resources import contents
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import lorem

from goods.models import Categories



def index(request):

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        'text_on_page':'Текст о том что магазин классный и товар отличный',
    }
    return render(request, "main/about.html", context)

def delivery(request):
    context = {
        "title": "Home - Доставка",
        "content": "Доставка и оплата",
        'text_on_page':'Мы доставляем вы оплачиваете',
    }
    return render(request, "main/delivery.html", context)

def info(request):
    context = {
        "title": "Home - Информация",
        "content": "Информация",
        'text_on_page':'Контактная информация',
    }
    return render(request, "main/info.html", context)

