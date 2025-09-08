from django.db import models
from leads.models import PotentialClient
from contracts.models import Contract


class ActiveClient(models.Model):
    """
    Модель активного клиента.
    Attributes:
        potential_client (OneToOneField): Связь с orm моделью PotentialClient.
        contract (OneToOneField): Связь с orm моделью Contract.
    """

    potential_client = models.OneToOneField(PotentialClient, on_delete=models.CASCADE)
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    