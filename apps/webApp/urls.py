from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('terms-of-service/', views.termsOfService, name='terms_of_service'),
    path('privacy-policy/', views.privacyPolicy, name='privacy_policy'),
    path('about/', views.about, name='about'),
    path('error/', views.error, name='error'),
    path('order/', views.order, name='order'),
    path('pricingImage/', views.pricingImage, name='pricing_image'),
]

