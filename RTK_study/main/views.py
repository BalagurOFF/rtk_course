import datetime
from django.shortcuts import render, redirect
from .models import RegionModel, NewsTopicsModel, NewsCommentsModel, NewsModel
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .forms import AddCommentForm, ContactForm


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
    if request.user.is_authenticated:
        form = ContactForm(initial={"name": request.user.get_full_name(), "email": request.user.email})
    else:
        form = ContactForm()
    return render(request, 'main/contacts.html', {'form': form})


def news(request):
    regions = RegionModel.objects.order_by('description')
    newstopics = NewsTopicsModel.objects.order_by('description')
    autors = User.objects.order_by('last_name')
    paginator = Paginator(NewsModel.objects.all().order_by('-date_pub')[:600], 12)
    page_number = request.GET.get('page')
    newslist = paginator.get_page(page_number)
    context = {'newslist': newslist, 'regions': regions, 'newstopics': newstopics, 'autors': autors}
    return render(request, 'main/news.html', context)


def new_full(request, id):
    comments = NewsCommentsModel.objects.filter(news_id=id)
    news_full = NewsModel.objects.get(pk=id)
    news_full.description = news_full.description.split('\r\n')
    last_news = NewsModel.objects.all().order_by('-date_pub').values('id', 'name')
    form = AddCommentForm()
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment_entry = form.save(commit=False)
            comment_entry.user = request.user
            comment_entry.news = news_full
            comment_entry.save()
    context = {
        'last_news': last_news,
        'news': news_full,
        'form': form,
        'comments': comments,
        }
    return render(request, 'main/newFull.html', context)


def handler404(request, exception):
    return render(request, '404.html')