from django.urls import path
from . import views

urlpatterns = [
    # order for below: path, view, name
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]

