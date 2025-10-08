import logging
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse, reverse_lazy
from .models import Product
from permissions import MarketerRequiredMixin

logger = logging.getLogger(__name__)


class ProductRetrieveView(MarketerRequiredMixin, DetailView):
    """
    View для вывода детальной информации о услуге
    """

    model = Product
    template_name = "products/products-detail.html"
    queryset = Product.objects.all()


class ProductCreateView(MarketerRequiredMixin, CreateView):
    """
    View для создание услуги
    """

    model = Product
    fields = "__all__"
    template_name = "products/products-create.html"
    success_url = reverse_lazy("products:products-list")

    def form_valid(self, form):
        logger.info(f"Создан новая услуга: {form.instance.title}")
        return super().form_valid(form)


class ProductListView(MarketerRequiredMixin, ListView):
    """
    View для вывода списка услуг
    """

    template_name = "products/products-list.html"
    model = Product
    context_object_name = "products"


class ProductDeleteView(MarketerRequiredMixin, DeleteView):
    """
    View для удаления услуги
    """

    template_name = "products/products-delete.html"
    model = Product
    success_url = reverse_lazy("products:products-list")


class ProductUpdateView(MarketerRequiredMixin, UpdateView):
    """
    View для изменения услуги
    """

    model = Product
    fields = "__all__"
    template_name = "products/products-edit.html"

    def form_valid(self, form):
        logger.info(f"Обновлёна услуга: {form.instance.title}")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("products:products-detail", kwargs={"pk": self.object.pk})
