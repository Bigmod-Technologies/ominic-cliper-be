from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from apps.webApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('terms-of-service/', views.termsOfService, name='terms_of_service'),
    path('privacy-policy/', views.privacyPolicy, name='privacy_policy'),
    path('about/', views.about, name='about'),
    path('error/', views.error, name='error'),
    path('order/', views.order, name='order'),
    path('pricingImage/', views.pricingImage, name='pricing_image'),

    path('blog/', include('apps.blog.urls')),

    #Service app urls
    path('service/', include('apps.service.urls')),

    #CKeditor
    path("ckeditor5/", include('django_ckeditor_5.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
