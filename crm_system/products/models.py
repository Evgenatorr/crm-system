from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """
    Модель Product представляет услугу, которую можно продавать.
    Attributes:
        price (DecimalField): Стоимость услуги.
        name (CharField): Название услуги.
        description (TextField): Описание услуги.
    """

    class Meta:
        ordering = ["title", "price"]

    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Стоимость услуги'
    )
    title = models.CharField(max_length=30, db_index=True, verbose_name='Название услуги')
    description = models.TextField(
        max_length=150,
        null=False,
        blank=True,
        verbose_name='Описание услуги'
    )
    
    def __str__(self) -> str:
        return self.title
