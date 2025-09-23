from django.urls import path
from .views import CustomerRetrieveView, CustomerCreateView, CustomerListView, CustomerDeleteView, CustomerUpdateView


app_name = "customers"


urlpatterns = [
    path("customers", CustomerListView.as_view(), name='customers-list'),
    path("customers/<int:pk>", CustomerRetrieveView.as_view(), name='customers-detail'),
    path("customers/create", CustomerCreateView.as_view(), name='customers-create'),
    path("customers/<int:pk>/edit", CustomerUpdateView.as_view(), name='customers-update'),
    path("customers/<int:pk>/delete", CustomerDeleteView.as_view(), name='customers-delete'),
]
