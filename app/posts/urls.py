from django.urls import path
from .views import *

urlpatterns = [
    path("post", PostViews, name="post"),
]
