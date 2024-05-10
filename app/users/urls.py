from django.urls import path
from .views import Home

app_name="users"

urlpatterns = [
    path("", Home,name="home"),
]
