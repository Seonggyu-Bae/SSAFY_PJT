from django.urls import path
from . import views

app_name = 'fas'

urlpatterns = [
    path('', views.index, name='index'),
    path('example/', views.example, name='example')
   
]