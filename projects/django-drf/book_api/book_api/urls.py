from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("library.urls")),
    path("api/v2/", include("library.urls_v2")),
]
