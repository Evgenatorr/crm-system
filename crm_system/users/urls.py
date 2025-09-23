from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import IndexView, MyLogoutView


app_name = "users"


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path(
        "login/",
        LoginView.as_view(
            template_name="registration/login.html",
        ),
        name="login",
    ),
    path("logout/", MyLogoutView.as_view(), name="logout"),
]
