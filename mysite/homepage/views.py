from django.shortcuts import render
from django.views import generic
from .models import *
from pure_pagination.mixins import PaginationMixin

class Top(generic.TemplateView):
    template_name = "homepage/top.html"
    model = Myinfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myinfo"] = self.model.objects.all()[0]
        context["works"] = Work.objects.filter(is_public=True)[:3]
        context["blogs"] = Blog.objects.filter(is_public=True)[:3]
        return context


class Myblog(PaginationMixin, generic.ListView):
    template_name = "homepage/myblog.html"
    model = Blog
    context_object_name = "blogs"
    paginate_by = 3
    
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)


class Works(PaginationMixin, generic.ListView):
    template_name = "homepage/works.html"
    model = Work
    context_object_name = "works"
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)