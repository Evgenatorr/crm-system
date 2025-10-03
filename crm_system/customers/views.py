from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse, reverse_lazy
from .models import ActiveClient
from permissions import ManagerRequiredMixin


class CustomerRetrieveView(ManagerRequiredMixin, DetailView):
    model = ActiveClient
    template_name = "customers/customers-detail.html"
    queryset = ActiveClient.objects.all()


class CustomerCreateView(ManagerRequiredMixin, CreateView):
    model = ActiveClient
    fields = "__all__"
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("customers:customers-list")


class CustomerListView(ManagerRequiredMixin, ListView):
    template_name = "customers/customers-list.html"
    model = ActiveClient
    context_object_name = "customers"


class CustomerDeleteView(ManagerRequiredMixin, DeleteView):
    template_name = "customers/customers-delete.html"
    model = ActiveClient
    success_url = reverse_lazy("customers:customers-list")


class CustomerUpdateView(ManagerRequiredMixin, UpdateView):
    model = ActiveClient
    fields = "__all__"
    template_name = "customers/customers-edit.html"

    def get_success_url(self):
        return reverse("customers:customers-detail", kwargs={"pk": self.object.pk})
