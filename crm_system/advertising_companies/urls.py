from django.urls import path
from .views import (
    AdvertisingRetrieveView,
    AdvertisingCreateView,
    AdvertisingListView,
    AdvertisingDeleteView,
    AdvertisingUpdateView,
)


app_name = "advertising_companies"


urlpatterns = [
    path("ads", AdvertisingListView.as_view(), name="ads-list"),
    path("ads/<int:pk>", AdvertisingRetrieveView.as_view(), name="ads-detail"),
    path("ads/create", AdvertisingCreateView.as_view(), name="ads-create"),
    path("ads/<int:pk>/edit", AdvertisingUpdateView.as_view(), name="ads-update"),
    path("ads/<int:pk>/delete", AdvertisingDeleteView.as_view(), name="ads-delete"),
]
