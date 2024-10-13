from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("apps.auth0.urls")),
    path("blog/", include("apps.blog.urls")),
    path("service/", include("apps.service.urls")),
    path("testimonial/", include("apps.testimonial.urls")),
    # Optional UI:
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("doc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # webApp
    # path('', include('apps.webApp.urls')),
    # #Service app urls
    # path('service/', include('apps.service.urls')),
    # #CKeditor
    # path("ckeditor5/", include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
