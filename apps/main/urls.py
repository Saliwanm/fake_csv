from django.urls import path
from . import views


urlpatterns = [
    path("", views.sign_in, name="sign_in"),
    path("logout", views.logout_view, name="logout"),
]