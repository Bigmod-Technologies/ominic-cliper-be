from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.blogDetails, name='blog_details'),
]