from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path("dashboard/", include("Dashboard.urls")),
    path("Dashboard/", include("Dashboard.urls")),
    path("", include("Dashboard.urls")),
	path("admin/", admin.site.urls),
]