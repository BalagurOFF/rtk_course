import datetime

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q, Value, F, CharField
from django.db.models import Count
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TagsModel, PublicationsCommentsModel, PublicationsModel, ContactModel
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from .forms import AddCommentForm, ContactForm
from django.views.generic import ListView, DetailView


User=get_user_model()
def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    if request.user.is_authenticated:
        form = ContactForm(initial={"sender": request.user.get_full_name(), "contact": request.user.email})
    else:
        form = ContactForm()
    return render(request, 'main/contacts.html', {'form': form})


class ContactMessages(PermissionRequiredMixin, ListView):
    permission_required = 'main.view_messages'
    model = ContactModel
    template_name = 'main/contactmessages.html'
    context_object_name = 'messages'
    paginate_by = 20


class ContactMessageDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'main.view_messages'
    model = ContactModel
    template_name = 'main/contactmessagedetail.html'
    context_object_name = 'message'


def news(request):
    if request.method == 'POST':
        search_string = request.POST.get('search_string')
        paginator = Paginator(PublicationsModel.objects.filter(Q(show_news = True) &
                                                       (
                                                            Q(title__icontains=search_string) |
                                                            Q(text__icontains=search_string) |
                                                            Q(autor__last_name__icontains=search_string) |
                                                            Q(autor__first_name__icontains=search_string) |
                                                            Q(tags__description__icontains=search_string)
                                                       )
        ).annotate(comments=Count('publicationscommentsmodel', distinct=True),
                    newsautor = Concat(F('autor__last_name'), Value(' '), F('autor__first_name'), output_field=CharField())).order_by('-date_pub')[:600], 12)
        page_number = request.GET.get('page')
        newslist = paginator.get_page(page_number)
        context = {'newslist': newslist}
    else:
        paginator = Paginator(PublicationsModel.objects.filter(show_news = True).annotate(comments=Count('publicationscommentsmodel', distinct=True),
                                                         newsautor = Concat(F('autor__last_name'), Value(' '), F('autor__first_name'), output_field=CharField())).order_by('-date_pub')[:600], 12)
        page_number = request.GET.get('page')
        newslist = paginator.get_page(page_number)
        context = {'newslist': newslist}
    return render(request, 'main/news.html', context)


def new_full(request, id):
    news_full = PublicationsModel.objects.select_related('autor').get(pk=id)
    comments = news_full.publicationscommentsmodel_set.select_related('user').values('date_comment', 'text', 'user__first_name', 'user__last_name', 'show_comment')
    news_full.description = news_full.description.split('\r\n')
    last_news = PublicationsModel.objects.order_by('-date_pub').all().values('id', 'name')
    form = AddCommentForm()
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment_entry = form.save(commit=False)
            comment_entry.user = request.user
            comment_entry.news = news_full
            comment_entry.save()
            form = AddCommentForm()
    context = {
        'last_news': last_news,
        'news': news_full,
        'form': form,
        'comments': comments,
        }
    return render(request, 'main/newFull.html', context)


def handler404(request, exception):
    return render(request, '404.html')


def handler403(request, exception):
    return render(request, '403.html')


@permission_required(['moderation'], raise_exception=True)
def moderation(request):
    print(request.POST)
    if request.method == 'POST':
        comment = request.POST['comment']
        if request.POST['status'] == 'true':
            status = True
        else:
            status = False
        PublicationsCommentsModel.objects.filter(id=comment).update(show_comment=status)
    return HttpResponse(None)
