from django.urls import path
from .views import ContractRetrieveView, ContractCreateView, ContractListView, ContractDeleteView, ContractUpdateView


app_name = "contracts"


urlpatterns = [
    path("contracts", ContractListView.as_view(), name='contracts-list'),
    path("contracts/<int:pk>", ContractRetrieveView.as_view(), name='contracts-detail'),
    path("contracts/create", ContractCreateView.as_view(), name='contracts-create'),
    path("contracts/<int:pk>/edit", ContractUpdateView.as_view(), name='contracts-update'),
    path("contracts/<int:pk>/delete", ContractDeleteView.as_view(), name='contracts-delete'),
]
