from django.shortcuts import render , get_object_or_404
from .models import *

def article_view(request) :
    articles = Article.objects.published().order_by('-created')
    context = {
        'articles' : articles,
    }
    return render(request , 'blog/home.html' , context)

def article_detail(request , slug) :    
    data = get_object_or_404(Article.objects.published() , slug=slug)
    context = {
        'article' : data,
    }
    return render(request , 'blog/detail.html', context)

def category(request , slug) :
    data = get_object_or_404(Category , slug=slug , status=True)
    context = {
        'category' : data,
    }
    return render(request , 'blog/category.html', context)