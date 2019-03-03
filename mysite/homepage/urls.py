from . import views
from django.urls import path

app_name = 'homepage'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('info/', views.Myinfo.as_view(), name='myinfo'),
    path('myblog/', views.Myblog.as_view(), name='myblog'),
    path('works/', views.Works.as_view(), name='works'),
]
