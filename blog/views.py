from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import *

def pagination(request ,list , count) :
    paginate = Paginator(list , count)
    page_number = request.GET.get('page')
    return paginate.get_page(page_number)

def article_view(request) :
    articles = Article.objects.published().order_by('-created')
    articles = pagination(request , articles , 1)
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
    data = get_object_or_404(Category , status=True , slug=slug)
    # data = pagination(request , data , 1)
    context = {
        'category' : data,
    }
    return render(request , 'blog/category.html', context)