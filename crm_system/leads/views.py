import logging
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


logger = logging.getLogger(__name__)


class LeadRetrieveView(OperatorRequiredMixin, DetailView):
    """
    View для вывода детальной информации о потенциальном клиенте
    """

    model = PotentialClient
    template_name = "leads/leads-detail.html"
    queryset = PotentialClient.objects.all()


class LeadCreateView(OperatorRequiredMixin, CreateView):
    """
    View для создания потенциального клиента
    """

    model = PotentialClient
    fields = "__all__"
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("leads:leads-list")

    def form_valid(self, form):
        logger.info(f"Создан новый потенциальный клиент: {form.instance.first_name}")
        return super().form_valid(form)


class LeadListView(OperatorRequiredMixin, ListView):
    """
    View для вывода списка потенциальных клиентов
    """

    template_name = "leads/leads-list.html"
    model = PotentialClient
    context_object_name = "leads"


class LeadDeleteView(OperatorRequiredMixin, DeleteView):
    """
    View для удаления потенциального клиента
    """

    template_name = "leads/leads-delete.html"
    model = PotentialClient
    success_url = reverse_lazy("leads:leads-list")


class LeadUpdateView(OperatorRequiredMixin, UpdateView):
    """
    View для изменения потенциального клиента
    """

    model = PotentialClient
    fields = "__all__"
    template_name = "leads/leads-edit.html"

    def get_success_url(self):
        return reverse("leads:leads-detail", kwargs={"pk": self.object.pk})
    
    def form_valid(self, form):
        logger.info(f"Изменен потенциальный клиент: {form.instance.first_name}")
        return super().form_valid(form)
