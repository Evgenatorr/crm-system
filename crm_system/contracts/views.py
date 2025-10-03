from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse, reverse_lazy
from .models import Contract
from .forms import ContractForm
from permissions import ManagerRequiredMixin


class ContractRetrieveView(ManagerRequiredMixin, DetailView):
    model = Contract
    template_name = "contracts/contracts-detail.html"
    queryset = Contract.objects.all()


class ContractCreateView(ManagerRequiredMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts-create.html"
    success_url = reverse_lazy("contracts:contracts-list")


class ContractListView(ManagerRequiredMixin, ListView):
    template_name = "contracts/contracts-list.html"
    model = Contract
    context_object_name = "contracts"


class ContractDeleteView(ManagerRequiredMixin, DeleteView):
    template_name = "contracts/contracts-delete.html"
    model = Contract
    success_url = reverse_lazy("contracts:contracts-list")


class ContractUpdateView(ManagerRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts-edit.html"

    def get_success_url(self):
        return reverse("contracts:contracts-detail", kwargs={"pk": self.object.pk})
