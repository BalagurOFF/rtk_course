from django.contrib import admin
from .models import *


class TagsAdmin(admin.ModelAdmin):
    list_display = ['description']
    list_filter = ['description']
    search_fields = ['description']


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'autor', 'date_pub', 'show_news']
    list_filter = ['title', 'autor', 'date_pub', 'show_news']
    autocomplete_fields = ['tags']
    search_fields = ['title', 'autor__username', 'autor__last_name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['date_message', 'sender', 'contact', 'message']


admin.site.register(TagsModel, TagsAdmin)
admin.site.register(PublicationsModel, PublicationsAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(ImagesModel)
