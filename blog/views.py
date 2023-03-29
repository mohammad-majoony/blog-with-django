from django.shortcuts import render , get_object_or_404
from .models import *

def article_view(request) :
    data = Article.objects.filter(status='p').order_by('-created')
    context = {
        'articles' : data,
    }
    return render(request , 'blog/home.html' , context)

def article_detail(request , slug) :    
    data = Article.objects.get(slug=slug)
    context = {
        'article' : data,
    }
    return render(request , 'blog/detail.html', context)