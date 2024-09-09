from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.service, name='service'),
    path('details/<slug:slug>/', views.serviceDetails, name='service_details'),
    path('portfolio/', views.servicePortfolio, name='service_portfolio'),
]