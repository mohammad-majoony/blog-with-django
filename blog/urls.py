from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('' , article_view , name='article_view'),
    path('<slug:slug>' , article_detail , name='article_detail'),
]
