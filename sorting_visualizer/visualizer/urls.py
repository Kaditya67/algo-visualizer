from django.urls import path
from . import views

urlpatterns = [
    path('', views.sort_visualizer, name='sort_visualizer'),
]
