from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse, reverse_lazy
from .models import Advertising
from permissions import MarketerRequiredMixin


class AdvertisingRetrieveView(MarketerRequiredMixin, DetailView):
    """
    View для вывода детальной информации о рекламной компании
    """
    
    model = Advertising
    template_name = "ads/ads-detail.html"
    queryset = Advertising.objects.all()


class AdvertisingCreateView(MarketerRequiredMixin, CreateView):
    """
    View для создания рекламной компании
    """
    
    model = Advertising
    fields = "__all__"
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("advertising_companies:ads-list")


class AdvertisingListView(MarketerRequiredMixin, ListView):
    """
    View для вывода списка рекламных компаний
    """
    
    template_name = "ads/ads-list.html"
    model = Advertising
    context_object_name = "ads"


class AdvertisingDeleteView(MarketerRequiredMixin, DeleteView):
    """
    View для удаления рекламной компании
    """
    
    template_name = "ads/ads-delete.html"
    model = Advertising
    success_url = reverse_lazy("advertising_companies:ads-list")


class AdvertisingUpdateView(MarketerRequiredMixin, UpdateView):
    """
    View для изменения рекламной компании
    """
    
    model = Advertising
    fields = "__all__"
    template_name = "ads/ads-edit.html"

    def get_success_url(self):
        return reverse("advertising_companies:ads-detail", kwargs={"pk": self.object.pk})


class AdvertisingStatisticView(MarketerRequiredMixin, ListView):
    """
    View для вывода статистики рекламной компании
    """
    
    template_name = 'ads/ads-statistic.html'
    model = Advertising
    context_object_name = "ads"
