from django.http import HttpResponse
from django.shortcuts import render

from ourteam.models import *

menu = ['Про команду', 'Вхід', 'Регестрація']

def index(request):
    posts = Ourteam.objects.all()
    return render(request, 'ourteam/index.html', {'posts': posts, 'menu': menu, 'title': 'Головна сторынка'})

def about(request):
    return render(request, 'ourteam/about.html', {'menu': menu, 'title': 'Про команду'})

def categories(request, catid):
    return HttpResponse(f"<h2>Виберіть учасника для перегляду іформації<h2><p>{catid}<p>")