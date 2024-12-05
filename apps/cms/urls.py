from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("content", views.PageContentView, basename="content")
router.register("metadata", views.MetadataView, basename="metadata")


urlpatterns = [path("", include(router.urls))]
