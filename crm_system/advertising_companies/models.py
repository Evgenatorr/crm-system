from django.db import models
from django.core.validators import MinValueValidator


class Advertising(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    promotion_channel = ...
    budget = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
