from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('' , article_view , name='home'),
    path('article/<slug:slug>' , article_detail , name='article_detail'),
    path('category/<slug:slug>' , category , name='category'),
]
