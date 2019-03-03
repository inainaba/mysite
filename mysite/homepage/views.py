from django.shortcuts import render
from django.views import generic
from .models import *


class Top(generic.TemplateView):
    template_name = "homepage/top.html"


class Myinfo(generic.TemplateView):
    template_name = "homepage/myinfo.html"


class Myblog(generic.ListView):
    template_name = "homepage/myblog.html"


class Works(generic.ListView):
    template_name = "homepage/works.html"