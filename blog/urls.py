from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('' , ArticlesView.as_view() , name='home'),
    path('page/<int:page>' , ArticlesView.as_view() , name='home'),
    path('article/<slug:slug>' , ArticleDetail.as_view() , name='article_detail'),
    path('category/<slug:slug>' , CategoryView.as_view() , name='category'),
    path('category/<slug:slug>/page/<int:page>' , CategoryView.as_view() , name='category'),
    
    path('author/<slug:username>/articles' , AuthorArticles.as_view() , name='author_articles'),
    path('author/<slug:username>/articles/page/<int:page>' , AuthorArticles.as_view() , name='author_articles'),
]
