from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet


app_name = "users"

routers = DefaultRouter()
routers.register("employee", EmployeeViewSet)


urlpatterns = [
    path("api/", include(routers.urls)),
]
