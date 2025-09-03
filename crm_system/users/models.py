from django.db import models
from django.contrib.auth.models import User


class PotentialClient(models.Model):
    """
    Модель потенциального клиента.
    Attributes:
        user (OneToOneField): Связь один к одному с orm моделью User.
        full_name (CharField): Полное имя пользователя.
        email (EmailField): Email пользователя.
        phone (CharField): Телефон пользователя.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(
        max_length=60, blank=True, null=True, verbose_name="Полное имя"
    )
    email = models.EmailField(max_length=254, unique=True)
    phone = models.PositiveIntegerField(
        blank=True, null=True, unique=True, verbose_name="Номер телефона"
    )
