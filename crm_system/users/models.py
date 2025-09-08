from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    """
    Модель сотрудника компании.
    Attributes:
        user (OneToOneField): Связь с orm моделью User.
        role (CharField): Должность сотрудника.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=100, verbose_name="Должность")
