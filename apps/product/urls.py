from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("price", views.PriceView, basename="price")
router.register("sample", views.SampleView, basename="sample")


urlpatterns = [path("", include(router.urls))]
