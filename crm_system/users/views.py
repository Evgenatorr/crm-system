from rest_framework import viewsets
from django.views.generic import TemplateView
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class IndexView(TemplateView):
    template_name = 'users/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = ...
        return context
    