from django.urls import path
from .views import ProductRetrieveView, ProductCreateView, ProductListView, ProductDeleteView, ProductUpdateView


app_name = "products"


urlpatterns = [
    path("products", ProductListView.as_view(), name='products-list'),
    path("products/<int:pk>", ProductRetrieveView.as_view(), name='products-detail'),
    path("products/create", ProductCreateView.as_view(), name='products-create'),
    path("products/<int:pk>/edit", ProductUpdateView.as_view(), name='products-update'),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name='products-delete'),
]
