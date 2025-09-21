from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse, reverse_lazy
from .models import Product


class ProductRetrieveView(DetailView):
    model = Product
    template_name = "products/products-detail.html"
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    template_name = "products/products-create.html"
    success_url = reverse_lazy("products:products-list")


class ProductListView(ListView):
    template_name = "products/products-list.html"
    model = Product
    context_object_name = "products"


class ProductDeleteView(DeleteView):
    template_name = "products/products-delete.html"
    model = Product
    success_url = reverse_lazy("products:products-list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "products/products-edit.html"

    def get_success_url(self):
        return reverse("products:products-detail", kwargs={"pk": self.object.pk})
