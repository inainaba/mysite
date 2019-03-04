from django.shortcuts import render
from django.views import generic
from .models import *


class Top(generic.TemplateView):
    template_name = "homepage/top.html"


class Myinfo(generic.TemplateView):
    template_name = "homepage/myinfo.html"
    model = Myinfo
    context_object_name = "myinfo"


class Myblog(generic.ListView):
    template_name = "homepage/myblog.html"
    model = Blog
    context_object_name = "blogs"

class Works(generic.ListView):
    template_name = "homepage/works.html"
    model = Work
    context_object_name = "works"