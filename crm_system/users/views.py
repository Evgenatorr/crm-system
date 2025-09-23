from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from products.models import Product
from customers.models import ActiveClient
from leads.models import PotentialClient
from advertising_companies.models import Advertising


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'users/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Product.objects.all().count()
        context["advertisements_count"] = Advertising.objects.all().count()
        context["leads_count"] = PotentialClient.objects.all().count()
        context["customers_count"] = ActiveClient.objects.all().count()
        return context
    

class MyLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")
    