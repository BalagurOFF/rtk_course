from django.contrib import admin
from .models import *
from contentmanagment.forms import AddNewsForm


class RegionAdmin(admin.ModelAdmin):
    list_display = ['description']
    list_filter = ['description']
    search_fields = ['description']


class NewsTopicsAdmin(admin.ModelAdmin):
    list_display = ['description']
    list_filter = ['description']
    search_fields = ['description']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'autor', 'date_pub', 'show_news']
    list_filter = ['name', 'autor', 'date_pub', 'show_news']
    autocomplete_fields = ['region', 'topicnews']
    search_fields = ['name', 'autor__username', 'autor__last_name']


admin.site.register(RegionModel, RegionAdmin)
admin.site.register(NewsTopicsModel, NewsTopicsAdmin)
admin.site.register(NewsModel, NewsAdmin)