from django.contrib import admin

# Register your models here.

from.models import Task, Activities

admin.site.register(Task)
admin.site.register(Activities)