from django.contrib import admin
from django.urls import path
from apps.webApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/details/', views.blogDetails, name='blog_details'),
    path('terms-of-service/', views.termsOfService, name='terms_of_service'),
    path('privacy-policy/', views.privacyPolicy, name='privacy_policy'),
    path('about/', views.about, name='about'),
    path('error/', views.error, name='error'),
    path('order/', views.order, name='order'),
    path('pricingImage/', views.pricingImage, name='pricing_image'),
    path('service/', views.service, name='service'),
    path('service/details/', views.serviceDetails, name='service_details'),
    path('service/portfolio/', views.servicePortfolio, name='service_portfolio'),
]