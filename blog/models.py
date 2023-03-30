from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from extensions.utils import jalali_converter 

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
    
    def __str__(self) :
        return self.title[:15]  
    
    class Meta :
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        
    def jalali_created(self) :
        return jalali_converter(self.created)
    
    jalali_created.short_description = 'زمان انتشار' 