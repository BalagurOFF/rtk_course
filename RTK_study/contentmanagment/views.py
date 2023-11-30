from django.shortcuts import render, redirect

from .forms import AddNewsForm, TagsForm
from main.models import NewsModel, TagsModel


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
            form.save_m2m()

        else:
            print("Форма не валидна")
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


def tags(request, id=None):
    tags = TagsModel.objects.all()
    form = TagsForm()
    if id != None:
        instance = TagsModel.objects.get(pk=id)
        form = TagsForm(instance=instance)
    if request.method == 'POST':
        form = TagsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('contentmanagment:tags', permanent=True)
    context = {
        'tags': tags,
        'form': form,
        'id': id,
    }
    print(form.instance)
    return render(request, 'contentmanagment/tags.html', context)
