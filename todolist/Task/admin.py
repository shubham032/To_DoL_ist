from django.contrib import admin
from.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')
    list_display_links = ('name',)

admin.site.register(Task, TaskAdmin)