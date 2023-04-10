from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter 

# my managers

class ArticleManger(models.Manager) :
    def published(self) :
        return self.filter(status="p")
    
class CategoryManger(models.Manager) :
    def active(self) :
        return self.filter(status=True)

class Category(models.Model) :
    parent = models.ForeignKey('self' , default=None , blank=True , null=True , related_name='children' , verbose_name='زیر دسته' , on_delete=models.SET_NULL)
    title = models.CharField(verbose_name = 'عنوان دسته بندی' , max_length=200)
    slug = models.SlugField(verbose_name = 'ادرس دسته بندی' , max_length=100 , unique=True)
    status = models.BooleanField(verbose_name = 'نمایش داده شود ؟' , default=True)
    position = models.IntegerField(verbose_name='پوزیشن')
    photo = models.ImageField(upload_to="categoryPic" , default="defualt/blog.jpg")
    
    class Meta :
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['-position'] 
    
    def __str__(self) :
        return self.title
    
    objects = CategoryManger()


class Article(models.Model) :
    STATUS_CHOICES = (
        ('d' , 'پرایوت'),
        ('p' , 'پابلیک') 
    )
    title = models.CharField(verbose_name = 'عنوان' , max_length=200)
    slug = models.SlugField(verbose_name = 'عنوان جستجو' , max_length=100 , unique=True)
    description = models.TextField(verbose_name = 'متن')
    thumbnail = models.ImageField(verbose_name = 'تامبنیل' , upload_to='images' , default="defualt/blog.jpg")
    created = models.DateTimeField(verbose_name = 'زمان انتشار' , auto_now_add=True)
    updated = models.DateTimeField(verbose_name = 'زمان بروزرسانی'  , auto_now=True)
    status = models.CharField(verbose_name = 'وضعیت' , max_length=1 , choices=STATUS_CHOICES)
    author = models.ForeignKey( get_user_model() , verbose_name = 'نویسنده' , on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name='دسته بندی' , related_name='articles')
    
    def __str__(self) :
        return self.title[:15]  
    
    class Meta :
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        
    def jalali_created(self) :
        return jalali_converter(self.created)
    jalali_created.short_description = 'زمان انتشار' 
    
    def category_public(self) :
        return self.category.filter(status=True)
    
    def thumbnail_html(self) :
        return format_html(f'<img src="{self.thumbnail.url}" style="height:40px ; width:60px;">')
    thumbnail_html.short_description = 'تامبنیل'
    
    objects = ArticleManger()