from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_completed', 'created_at', 'updated_at']
    search_fields = ['title']


admin.site.register(Task, TaskAdmin)
