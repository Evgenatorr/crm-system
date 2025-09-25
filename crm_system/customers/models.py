from django.db import models
from leads.models import PotentialClient
from contracts.models import Contract
from advertising_companies.models import Advertising


class ActiveClient(models.Model):
    """
    Модель активного клиента.
    Attributes:
        potential_client (OneToOneField): Связь с orm моделью PotentialClient.
        contract (OneToOneField): Связь с orm моделью Contract.
    """

    potential_client = models.OneToOneField(PotentialClient, on_delete=models.CASCADE)
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    advertising = models.ForeignKey(
        Advertising, on_delete=models.CASCADE, related_name="active_clients", default=1
    )
    