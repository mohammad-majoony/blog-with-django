from django.contrib import admin
from .models import *

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin) :
    list_display = ['title' , 'author' , 'jalali_created' , 'category_str' , 'status']
    list_editable = ['status']
    list_filter = ['status']
    prepopulated_fields = {'slug' : ('title' ,)}
    ordering = ["-created"]
    
    def category_str(self , obj) :
        return " - ".join([category.title for category in obj.category_public()])
    category_str.short_description = 'دسته بندی ها'
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin) :
    list_display = ['position' ,'title' , 'parent' , 'status']
    list_editable = ['status']
    list_filter = ['status']
    ordering = ["parent__id" , "-position"]
    prepopulated_fields = {'slug' : ('title' ,)}