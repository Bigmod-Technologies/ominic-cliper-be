from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("contact-message", views.ContactMessageView, basename="contact-message")

urlpatterns = [path("", include(router.urls))]
