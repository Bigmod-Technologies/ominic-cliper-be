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
    path("order/", include("apps.order.urls")),
    path("crm/", include("apps.crm.urls")),
    path("product/", include("apps.product.urls")),
    # Optional UI:
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("doc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
