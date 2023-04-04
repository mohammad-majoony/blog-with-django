from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import *

def pagination(list , count , page) :
    paginate = Paginator(list , count)
    return paginate.get_page(page)

def article_view(request , page = 1) :
    articles = Article.objects.published().order_by('-created')
    articles = pagination(articles , 1 , page)
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

def category(request , slug , page=1) :
    category = get_object_or_404(Category , status=True , slug=slug)
    articles = category.articles.published()
    articles = pagination(articles , 2 , page)
    context = {
        'category' : category,
        'articles' : articles
    }
    return render(request , 'blog/category.html', context)