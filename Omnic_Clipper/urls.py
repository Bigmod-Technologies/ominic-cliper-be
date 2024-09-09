from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #webApp
    path('', include('apps.webApp.urls')),

    path('blog/', include('apps.blog.urls')),

    #Service app urls
    path('service/', include('apps.service.urls')),

    #CKeditor
    path("ckeditor5/", include('django_ckeditor_5.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
