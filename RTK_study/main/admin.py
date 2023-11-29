from django.contrib import admin
from .models import *
from contentmanagment.forms import AddNewsForm


class TagsAdmin(admin.ModelAdmin):
    list_display = ['description']
    list_filter = ['description']
    search_fields = ['description']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'autor', 'date_pub', 'show_news']
    list_filter = ['name', 'autor', 'date_pub', 'show_news']
    autocomplete_fields = ['tags']
    search_fields = ['name', 'autor__username', 'autor__last_name']


admin.site.register(TagsModel, TagsAdmin)
admin.site.register(NewsModel, NewsAdmin)
