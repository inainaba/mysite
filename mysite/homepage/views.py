from django.shortcuts import render
from django.views import generic
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Top(generic.TemplateView):
    template_name = "homepage/top.html"
    model = Myinfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myinfo"] = self.model.objects.all()[0]
        return context


class Myblog(generic.ListView):
    template_name = "homepage/myblog.html"
    model = Blog
    context_object_name = "blogs"
    paginate_by = 3
    
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True).order_by('-date_birth')


class Works(generic.ListView):
    template_name = "homepage/works.html"
    model = Work
    context_object_name = "works"
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True).order_by('-date_birth')