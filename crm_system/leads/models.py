from django.db import models

from advertising_companies.models import Advertising


class PotentialClient(models.Model):
    """
    Модель потенциального клиента.
    Attributes:
        full_name (CharField): Полное имя пользователя.
        email (EmailField): Email пользователя.
        phone (CharField): Телефон пользователя.
        advertising (ForeignKey): Связь с orm моделью Advertising.
    """

    full_name = models.CharField(
        max_length=60, blank=True, null=True, verbose_name="Полное имя"
    )
    email = models.EmailField(max_length=254, unique=True)
    phone = models.PositiveIntegerField(
        blank=True, null=True, unique=True, verbose_name="Номер телефона"
    )
    advertising = models.ForeignKey(
        Advertising, on_delete=models.CASCADE, related_name="potential_clients"
    )
