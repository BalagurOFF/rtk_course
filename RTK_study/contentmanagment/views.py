import datetime
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import F, CharField, Q
from django.db.models.functions import Concat
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission
from .forms import AddNewsForm, TagsForm
from main.models import NewsModel, TagsModel, ImagesModel


User = get_user_model()


def addnews(request, news_id=None):
    context = {}
    if news_id:
        instance = NewsModel.objects.get(pk=news_id)
        form = AddNewsForm(instance=instance)
    else:
        instance = None
        form = AddNewsForm()
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            if id is None:
                news_entry = form.save(commit=False)
                news_entry.autor = request.user
                news_entry.save()
                form.save_m2m()
                for img in request.FILES.getlist('image_field'):
                    ImagesModel.objects.create(news=news_entry, image=img, description=img.name)
            else:
                news_entry = form.save()
                for img in request.FILES.getlist('image_field'):
                    ImagesModel.objects.create(news=news_entry, image=img, description=img.name)
        url_referer = request.session['url_referer']
        return HttpResponseRedirect(url_referer)
    request.session['url_referer'] = request.META.get('HTTP_REFERER')
    context['form'] = form
    context['news'] = instance
    return render(request, 'contentmanagment/addnews.html', context)


def newschange(request):
    newslist = NewsModel.objects.filter(autor=request.user).order_by('-date_pub')
    context = {'newslist': newslist}
    return render(request, 'contentmanagment/newslist.html', context)


def removenews(request, news_id):
    NewsModel.objects.filter(id=news_id).delete()
    return redirect('contentmanagment:news-list', permanent=True)


def tags(request, id=None):
    tags_news = TagsModel.objects.all()
    if id is not None:
        instance = TagsModel.objects.get(pk=id)
        form = TagsForm(instance=instance)
    else:
        form = TagsForm()
    if request.method == 'POST':
        if id is not None:
            instance = TagsModel.objects.get(pk=id)
            form = TagsForm(request.POST, instance=instance)
        else:
            form = TagsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contentmanagment:tags', permanent=True)
    context = {
        'tags': tags_news,
        'form': form,
        'id': id,
    }
    return render(request, 'contentmanagment/tags.html', context)


def moderation(request):
    print(request.POST)
    return None


def administratenews(request):
    date_start = datetime.date.today() - datetime.timedelta(days=30)
    date_end = datetime.date.today()
    autor_id = 0
    queryset = NewsModel.objects.filter(Q(date_pub__date__gte = date_start) & Q(date_pub__date__lte = date_end)).order_by('-date_pub')
    if request.method == 'POST':
        if request.POST['date_start']:
            date_start = datetime.datetime.strptime(request.POST['date_start'], "%Y-%m-%d")
            queryset = queryset.filter(date_pub__date__gte = date_start)
        if request.POST['date_end']:
            date_end = datetime.datetime.strptime(request.POST['date_end'], "%Y-%m-%d")
            queryset = queryset.filter(date_pub__date__lte = date_end)
        autor_id = int(request.POST['autor'])
        if autor_id != 0:
            queryset = queryset.filter(autor = autor_id)

    paginator = Paginator(queryset.distinct(), 20)
    page_number = request.GET.get('page')
    newslist = paginator.get_page(page_number)
    perm = Permission.objects.get(codename='add_newsmodel')
    autors = User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm)).distinct()
    context = {'newslist': newslist, 'autors': autors, 'date_start': date_start.strftime('%Y-%m-%d'), 'date_end': date_end.strftime('%Y-%m-%d'), 'autor_id': autor_id}
    return render(request, 'contentmanagment/adminlist.html', context)


def removetag(request, id=None):
    if id is not None:
        TagsModel.objects.filter(id=id).delete()
        return redirect('contentmanagment:tags', permanent=True)
