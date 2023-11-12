from django.shortcuts import render

from . import forms


# Create your views here.
def addnews(request):
    form = forms.AddNewsForm()
    return render(request, 'contentmanagment/addnews.html', {'form': form})