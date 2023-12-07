from django.contrib import admin
from .models import *


class TagsAdmin(admin.ModelAdmin):
    list_display = ['description']
    list_filter = ['description']
    search_fields = ['description']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'autor', 'date_pub', 'show_news']
    list_filter = ['name', 'autor', 'date_pub', 'show_news']
    autocomplete_fields = ['tags']
    search_fields = ['name', 'autor__username', 'autor__last_name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['date_message', 'sender', 'contact', 'message']


admin.site.register(TagsModel, TagsAdmin)
admin.site.register(NewsModel, NewsAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(ImagesModel)
