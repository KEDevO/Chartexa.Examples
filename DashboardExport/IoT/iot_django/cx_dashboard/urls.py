from django.urls import path
from . import views
urlpatterns = [
    path("",                    views.dashboard, name="dashboard"),
    path("api/dashboard",  views.api_dashboard, name="api_dashboard"),
]
