from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import *

class ArticleView(ListView) :
    queryset = Article.objects.filter(status='p').order_by('-created')
    context_object_name = 'articles'
    template_name = 'blog/home.html'
    
class ArticleDetail(DetailView) :
    model = Article
    context_object_name = 'article'
    template_name = 'blog/detail.html'