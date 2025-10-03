from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse, reverse_lazy
from .models import PotentialClient
from permissions import OperatorRequiredMixin


class LeadRetrieveView(OperatorRequiredMixin, DetailView):
    model = PotentialClient
    template_name = "leads/leads-detail.html"
    queryset = PotentialClient.objects.all()


class LeadCreateView(OperatorRequiredMixin, CreateView):
    model = PotentialClient
    fields = "__all__"
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("leads:leads-list")


class LeadListView(OperatorRequiredMixin, ListView):
    template_name = "leads/leads-list.html"
    model = PotentialClient
    context_object_name = "leads"


class LeadDeleteView(OperatorRequiredMixin, DeleteView):
    template_name = "leads/leads-delete.html"
    model = PotentialClient
    success_url = reverse_lazy("leads:leads-list")


class LeadUpdateView(OperatorRequiredMixin, UpdateView):
    model = PotentialClient
    fields = "__all__"
    template_name = "leads/leads-edit.html"

    def get_success_url(self):
        return reverse("leads:leads-detail", kwargs={"pk": self.object.pk})
