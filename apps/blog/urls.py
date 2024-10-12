from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("tags", views.BlogTagView, basename="blog_tag")
router.register("content", views.BlogView, basename="blog")

urlpatterns = [path("", include(router.urls))]
