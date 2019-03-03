from django.shortcuts import render
from django.views import generic
from .models import *


class Top(generic.TemplateView):
    template_name = "homepage/top"


class Myinfo(generic.TemplateView):
    template_name = "homepage/myinfo"


class Myblog(generic.ListView):
    template_name = "homepage/myblog"


class Works(generic.ListView):
    template_name = "homepage/works"