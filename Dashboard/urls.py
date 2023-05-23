from django.urls import include, path

from . import views

app_name = "Dashboard"
urlpatterns = [
    path("", views.index.as_view(), name="observation_list"),
]