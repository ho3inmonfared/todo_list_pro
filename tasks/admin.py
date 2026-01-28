from django.contrib import admin
from django.utils.text import Truncator

from . import models

@admin.register(models.Category)
class Category(admin.ModelAdmin):
    list_display=('title', )
    search_fields=('title', )
    

@admin.register(models.Task)
class Task(admin.ModelAdmin):
    list_display=('short_text', )
    list_filter=('category','created_at', )
    
    def short_text(self,obj):
        return Truncator(obj.text).words(5)