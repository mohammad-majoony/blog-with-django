from django.contrib import admin
from .models import *

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin) :
    list_display = ['title' , 'author' , 'created' , 'status']
    list_editable = ['status']
    list_filter = ['status']
    prepopulated_fields = {'slug' : ('title' ,)}
    ordering = ["-created"]