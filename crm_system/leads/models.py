from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from advertising_companies.models import Advertising


class PotentialClient(models.Model):
    """
    Модель потенциального клиента.
    Attributes:
        first_name (CharField): Имя пользователя.
        last_name (CharField): Фамилия пользователя.
        email (EmailField): Email пользователя.
        phone (CharField): Телефон пользователя.
        advertising (ForeignKey): Связь с orm моделью Advertising.
    """
    first_name = models.CharField(
        max_length=60, blank=True, null=True, verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=60, blank=True, null=True, verbose_name="Фамилия"
    )
    email = models.EmailField(max_length=254, unique=True, verbose_name='Почта')
    phone = PhoneNumberField(
        blank=True, null=True, unique=True, verbose_name="Номер телефона"
    )
    advertising = models.ForeignKey(
        Advertising, on_delete=models.CASCADE, related_name="potential_clients", verbose_name='Рекламная компания'
    )
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
