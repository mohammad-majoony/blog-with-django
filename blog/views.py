from django.shortcuts import render , get_object_or_404
from .models import *

def article_view(request) :
    data = Article.objects.filter(status='p').order_by('-created')
    context = {
        'articles' : data,
    }
    return render(request , 'blog/home.html' , context)

def article_detail(request , slug) :    
    data = get_object_or_404(Article , slug=slug , status='p')
    context = {
        'article' : data,
    }
    return render(request , 'blog/detail.html', context)