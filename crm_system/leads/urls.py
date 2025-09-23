from django.urls import path
from .views import LeadRetrieveView, LeadCreateView, LeadListView, LeadDeleteView, LeadUpdateView


app_name = "leads"


urlpatterns = [
    path("leads", LeadListView.as_view(), name='leads-list'),
    path("leads/<int:pk>", LeadRetrieveView.as_view(), name='leads-detail'),
    path("leads/create", LeadCreateView.as_view(), name='leads-create'),
    path("leads/<int:pk>/edit", LeadUpdateView.as_view(), name='leads-update'),
    path("leads/<int:pk>/delete", LeadDeleteView.as_view(), name='leads-delete'),
]
