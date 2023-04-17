from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.models import User

from django.views.generic import ListView , DetailView

def pagination(list , count , page) :
    paginate = Paginator(list , count)
    return paginate.get_page(page)

class ArticlesView(ListView) :
    queryset = Article.objects.published().order_by('-created')
    paginate_by = 1
    template_name = 'blog/home.html' # or change html name to articles_view.html in blog folder
    context_object_name = 'articles'
    

class ArticleDetail(DetailView) :
    def get_object(self) :
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published() , slug=slug)
    template_name = 'blog/detail.html' # or set html name to article_detail.html


class CategoryView(ListView) :
    template_name = 'blog/category.html'
    paginate_by = 1
    context_object_name = 'articles'
    
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active() , slug=slug)
        return category.articles.published()
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    
class AuthorArticles(ListView) :
    template_name = 'blog/author_articles.html'
    context_object_name = 'articles'
    paginate_by = 3 
    
    def get_queryset(self) :
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User , username=username)
        return author.articles.published()
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context