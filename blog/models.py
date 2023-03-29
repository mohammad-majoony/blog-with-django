from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Article(models.Model) :
    STATUS_CHOICES = (
        ('d' , 'draft'),
        ('p' , 'publish') 
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100 , unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images' , default="defualt/blog.jpg")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES)
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.title[:15]  