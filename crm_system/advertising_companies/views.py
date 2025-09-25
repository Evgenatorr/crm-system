from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Advertising


class AdvertisingRetrieveView(LoginRequiredMixin, DetailView):
    model = Advertising
    template_name = "ads/ads-detail.html"
    queryset = Advertising.objects.all()


class AdvertisingCreateView(LoginRequiredMixin, CreateView):
    model = Advertising
    fields = "__all__"
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("advertising_companies:ads-list")


class AdvertisingListView(LoginRequiredMixin, ListView):
    template_name = "ads/ads-list.html"
    model = Advertising
    context_object_name = "ads"


class AdvertisingDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "ads/ads-delete.html"
    model = Advertising
    success_url = reverse_lazy("advertising_companies:ads-list")


class AdvertisingUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertising
    fields = "__all__"
    template_name = "ads/ads-edit.html"

    def get_success_url(self):
        return reverse("advertising_companies:ads-detail", kwargs={"pk": self.object.pk})


class AdvertisingStatisticView(LoginRequiredMixin, ListView):
    template_name = 'ads/ads-statistic.html'
    model = Advertising
    context_object_name = "ads"
