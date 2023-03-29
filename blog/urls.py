from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('' , ArticleView.as_view() , name='article_view'),
    path('<slug:slug>' , ArticleDetail.as_view() , name='article_detail'),
]
