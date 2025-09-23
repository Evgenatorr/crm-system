from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("users.urls")),
    path("", include("products.urls")),
    path("", include("contracts.urls")),
    path("", include("leads.urls")),
    path("", include("advertising_companies.urls")),
    path("", include("customers.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]


if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
