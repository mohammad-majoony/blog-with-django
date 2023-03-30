from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('' , article_view , name='home'),
    path('<slug:slug>' , article_detail , name='article_detail'),
]
