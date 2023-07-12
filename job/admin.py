from django.contrib import admin
from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'type', 'price', 'working_day', 'created_date']


admin.site.register(Job, JobAdmin)
