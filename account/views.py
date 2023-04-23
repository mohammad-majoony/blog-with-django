from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from blog.models import *

class LoginComplate(LoginRequiredMixin , ListView) :
    queryset = Article.objects.all()
    context_object_name = 'articles' 
    template_name = 'registration/base.html'
    
    def get_queryset(self):
        global category
        if self.request.user.is_superuser :
            article = Article.objects.all()
        else :
            username = self.request.user
            article = Article.objects.filter(author=username)
        return article