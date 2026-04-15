from django.urls import include, path
urlpatterns = [
    path("", include("cx_dashboard.urls")),
]
