from django.contrib import admin
from .models import *

# admin.site.disable_action('delete_selected')

def text_message(count) :
    if count == 1 : return "شد"
    return "شدند"

def make_private(modeladmin , request , queryset) :
    count = queryset.update(status='d')
    verb = text_message(count)
    modeladmin.message_user(request , f"مخفی {verb}")
make_private.short_description = 'مخفی کردن پست'

def make_public(modeladmin, request, queryset):
    update = queryset.update(status="p")
    verb = text_message(update)
    modeladmin.message_user(request , f"انتشار داده  {verb}")
make_public.short_description = 'انتشار پست'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin) :
    list_display = ['title' , 'thumbnail_html' , 'author' , 'jalali_created' , 'category_str' , 'status']
    list_editable = ['status']
    list_filter = ['status' , 'author']
    prepopulated_fields = {'slug' : ('title' ,)}
    ordering = ["-created"]
    actions = [make_private , make_public]
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin) :
    list_display = ['position' ,'title' , 'parent' , 'status']
    list_editable = ['status']
    list_filter = ['status']
    ordering = ["parent__id" , "-position"]
    prepopulated_fields = {'slug' : ('title' ,)}