from django.core.paginator import Paginator
from django.db.models import F, CharField
from django.db.models.functions import Concat
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import AddNewsForm, TagsForm
from main.models import NewsModel, TagsModel


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
            else:
                form.save()
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
    paginator = Paginator(NewsModel.objects.all().order_by('-date_pub'), 20)
    page_number = request.GET.get('page')
    newslist = paginator.get_page(page_number)
    context = {'newslist': newslist}
    return render(request, 'contentmanagment/adminlist.html', context)


def removetag(request, id=None):
    if id is not None:
        TagsModel.objects.filter(id=id).delete()
        return redirect('contentmanagment:tags', permanent=True)
