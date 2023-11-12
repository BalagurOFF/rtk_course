import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import logout #, authenticate, login
from . import forms
from . import models
from django.contrib.auth import get_user_model
#from django.http import HttpResponse
# Create your views here.


User=get_user_model()
def about(request):
    context = [
        {'last_name': 'Лисенок', 
         'first_name': 'Алиса', 
         'description': 'Автор бизнесс-новостей', 
         'email': 'bizness@mail.ru'},
        {'last_name': 'Емелина', 
         'first_name': 'Ольга', 
         'description': 'Автор международных новостей', 
         'email': 'mir@mail.ru'},
        {'last_name': 'Кадюкова', 
         'first_name': 'Ксюша', 
         'description': 'Автор региональных новостей', 
         'email': 'region@mail.ru'},
        ]
    return render(request, 'main/about.html', {'persons' :context})


def contacts(request):
    context = [
        {'last_name': 'Филимонова', 
         'first_name': 'Надежда', 
         'description': 'Главный редактор', 
         'email': '123@mail.ru'},
        {'last_name': 'Григорьева', 
         'first_name': 'Ариана', 
         'description': 'Пресс-секретарь', 
         'email': '234@mail.ru'},
        {'last_name': 'Нуждин', 
         'first_name': 'Андрей', 
         'description': 'Администратор', 
         'email': 'admin@mail.ru'},
         ]
    return render(request, 'main/contacts.html', {'persons' :context})


def news(request):
    regions = models.RegionModel.objects.order_by('description')
    newstopics = models.NewsTopicsModel.objects.order_by('description')
    autors = User.objects.order_by('last_name')
    l = [
        {'id': 1, 'name': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure officiis hic cupiditate at impedit nihil necessitatibus ullam perferendis et. Iusto dicta quasi ipsa natus possimus est maiores sunt magnam architecto!', 'img': 'main/news/6.jpg'},
        {'id': 2, 'name': 'Новость 2', 'img': 'main/news/1.jpg'},
        {'id': 3, 'name': 'Новость 3', 'img': 'main/news/2.jpg'},
        {'id': 4, 'name': 'Новость 4', 'img': 'main/news/3.jpg'},
        {'id': 5, 'name': 'Новость 5', 'img': 'main/news/4.jpg'},
        {'id': 6, 'name': 'Новость 6', 'img': 'main/news/5.jpg'},
        {'id': 7, 'name': 'Новость 7', 'img': 'main/news/6.jpg'},
        {'id': 8, 'name': 'Новость 8', 'img': 'main/news/1.jpg'},
        {'id': 9, 'name': 'Новость 9', 'img': 'main/news/2.jpg'},
        {'id': 10, 'name': 'Новость 10', 'img': 'main/news/3.jpg'},
        {'id': 11, 'name': 'Новость 11', 'img': 'main/news/4.jpg'},
        {'id': 12, 'name': 'Новость 12', 'img': 'main/news/5.jpg'},
    ]
    context = { 'newslist': l, 'regions': regions, 'newstopics': newstopics, 'autors': autors}
    return render(request, 'main/news.html', context)


def new_full(request, id_new):
    context = {'id': id_new,
               'name': 'Новость №1',
               'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure officiis hic cupiditate at impedit nihil necessitatibus ullam perferendis et. Iusto dicta quasi ipsa natus possimus est maiores sunt magnam architecto!',
               'autor': 'Автор Б.В.',
               'datePublication': datetime.date(2023, 11, 8),
               'mainImage': 'main/news/1.jpg',
               'addititionalMaterials': ['main/news/2.jpg', 'main/news/3.jpg', 'main/news/4.jpg', 'main/news/5.jpg', 'main/news/6.jpg'],}
    return render(request, 'main/newFull.html', context)
