from django.contrib import admin

from .models import Contact, Subscribe


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message']
    date_hierarchy = 'created_date'
    search_fields = ['name', 'email']


admin.site.register(Contact, ContactAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


admin.site.register(Subscribe, SubscribeAdmin)
