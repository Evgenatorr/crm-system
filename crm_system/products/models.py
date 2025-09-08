from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Модель Product представляет товар, который можно продавать.
    Attributes:
        price (DecimalField): Стоимость товара.
        name (CharField): Название товара.
        description (TextField): Описание товара.
    """

    class Meta:
        ordering = ["name", "price"]

    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    name = models.CharField(max_length=30, db_index=True)
    description = models.TextField(
        max_length=150,
        null=False,
        blank=True,
    )
