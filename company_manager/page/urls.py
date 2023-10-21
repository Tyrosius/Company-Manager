from django.urls import path
from . import views

app_name = "page"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="page"),
]