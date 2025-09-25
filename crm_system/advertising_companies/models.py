from django.db import models
from django.core.validators import MinValueValidator

from products.models import Product


class PromotionChannels(models.IntegerChoices):
    """Каналы продвижения рекламной компании."""

    SITE = 1
    SOCIAL_NETWORK = 2
    INTEGRATION = 3


class Advertising(models.Model):
    """
    Модель рекламной компании.
    Attributes:
        title (CharField): Название рекламной компании.
        service (OneToOneField): Связь с orm моделью Product.
        promotion_channel (PositiveSmallIntegerField): Канал продвижения.
        budget (DecimalField): Бюджет рекламной компании.
    """

    title = models.CharField(max_length=40, verbose_name="Название рекламной компании")
    service = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="advertising"
    )
    promotion_channel = models.PositiveSmallIntegerField(
        verbose_name="Канал продвижения",
        choices=PromotionChannels.choices,
        default=PromotionChannels.SITE,
    )
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Бюджет",
    )

    @property
    def leads_count(self):
        return self.potential_clients.count()

    @property
    def customers_count(self):
        return self.active_clients.count()
    
    @property
    def profit(self):
        summ_contracts = self.service.contracts.all().aggregate(summ=models.Sum('cost'))
        budget_ads = self.budget
        result = summ_contracts['summ'] / budget_ads * 100
        return result
