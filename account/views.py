from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

@login_required
def login_complate(request) :
    return render(request , 'registration/login_complete.html')

class LoginComplate(LoginRequiredMixin , TemplateView) :
    template_name = 'registration/base.html'