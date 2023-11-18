from django.shortcuts import render, redirect

from .forms import AddNewsForm, NewsTopicsForm, RegionForm
from main.models import NewsModel, RegionModel, NewsTopicsModel


def addnews(request, news_id=None):
    print(request.user.id)
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
            news_entry = form.save(commit=False)
            news_entry.autor = request.user
            news_entry.save()
        return redirect('contentmanagment:news-list', permanent=True)
    context['form'] = form
    context['news'] = instance
    return render(request, 'contentmanagment/addnews.html', context)


def newschange(request):
    newslist = NewsModel.objects.filter(autor=request.user)
    context = {'newslist': newslist}
    return render(request, 'contentmanagment/newslist.html', context)


def removenews(request, news_id):
    entry = NewsModel.objects.filter(id=news_id)
    entry.delete()
    return redirect('contentmanagment:news-list', permanent=True)


def regions(request, id=None):
    regions = RegionModel.objects.all()
    form = RegionForm()
    if id != None:
        instance = RegionModel.objects.get(pk=id)
        form = RegionForm(instance=instance)
    context = {
        'regions': regions,
        'form': form,
        'id': id
    }
    return render(request, 'contentmanagment/regions.html', context)


def topics(request, id=None):
    newstopics = NewsTopicsModel.objects.all()
    form = NewsTopicsForm()
    if id != None:
        instance = NewsTopicsModel.objects.get(pk=id)
        form = NewsTopicsForm(instance=instance)
    context = {
        'newstopics': newstopics,
        'form': form,
        'id': id,
    }
    return render(request, 'contentmanagment/topics.html', context)
