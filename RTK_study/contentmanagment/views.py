import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import F, CharField, Q
from django.db.models.functions import Concat
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission
from django.views.generic import CreateView

from .forms import AddPublicationsForm, TagsForm, AddImageFormset
from main.models import PublicationsModel, TagsModel, ImagesModel
from django_addanother.views import CreatePopupMixin


User = get_user_model()


@permission_required(['main.publications_editor'], raise_exception=True)
def createpublication(request, id=None):
    template_name = 'contentmanagment/addnews.html'
    order_instance = PublicationsModel()
    if id is not None:
        order_instance = PublicationsModel.objects.get(pk=id)
    form = AddPublicationsForm(request.POST or None, instance=order_instance, prefix='main')
    formset = AddImageFormset(request.POST or None, request.FILES or None, instance=order_instance, prefix='images')
    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            news_entry = form.save(commit=False)
            if id is None:
                news_entry.autor = request.user
                news_entry.date_pub = datetime.datetime.now()
            news_entry.editor = request.user
            news_entry.save()
            form.save_m2m()
            formset.save()
            url_referer = request.session['url_referer']
            return HttpResponseRedirect(url_referer)
    request.session['url_referer'] = request.META.get('HTTP_REFERER')
    context = {'form': form, 'formset': formset, 'news': order_instance}
    return render(request, template_name, context)


@permission_required(['main.publications_editor'], raise_exception=True)
def newschange(request):
    newslist = PublicationsModel.objects.filter(autor=request.user).order_by('-date_pub')
    context = {'newslist': newslist}
    return render(request, 'contentmanagment/newslist.html', context)


@permission_required(['main.publications_editor', 'main.main_publications_editor'], raise_exception=True)
def removenews(request, news_id):
    PublicationsModel.objects.filter(id=news_id).delete()
    url_redirect = request.session['url_referer']
    print(url_redirect)
    return redirect(url_redirect, permanent=True)


@permission_required(['main.tags_editor'], raise_exception=True)
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


class TagCreate(CreatePopupMixin, CreateView):
    form_class = TagsForm
    model = TagsModel
    #fields = ['description']
    template_name = 'contentmanagment/tag_create.html'


@permission_required(['main.main_publications_editor'], raise_exception=True)
def administratenews(request):
    date_start = datetime.date.today() - datetime.timedelta(days=30)
    date_end = datetime.date.today()
    autor_id = 0
    queryset = PublicationsModel.objects.filter(Q(date_pub__date__gte = date_start) & Q(date_pub__date__lte = date_end)).order_by('-date_pub')
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
    perm = Permission.objects.get(codename='publications_editor')
    autors = User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm)).distinct()
    context = {'newslist': newslist, 'autors': autors, 'date_start': date_start.strftime('%Y-%m-%d'), 'date_end': date_end.strftime('%Y-%m-%d'), 'autor_id': autor_id}
    return render(request, 'contentmanagment/adminlist.html', context)


@permission_required(['main.tags_editor'], raise_exception=True)
def removetag(request, id=None):
    if id is not None:
        TagsModel.objects.filter(id=id).delete()
        return redirect('contentmanagment:tags', permanent=True)
