from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddNewsForm
from main.models import NewsModel


# Create your views here.
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
    newslist = NewsModel.objects.filter(autor = request.user)
    context = {'newslist': newslist}
    return render(request, 'contentmanagment/newslist.html', context)


def removenews(request, news_id):
    entry = NewsModel.objects.filter(id=news_id)
    entry.delete()
    return redirect('contentmanagment:news-list', permanent=True)