from django.db import models
from django.core.validators import MinValueValidator

from products.models import Product


def contract_document_directory_path(instance: "Contract", filename: str) -> str:
    """
    Функция возвращает путь для хранения документа
    Args:
        instance (Contract): Модель с файлом.
        filename (str): Имя файла с документом.

    Returns:
        str: Путь для хранения документа.
    """

    return "contracts/contract_{pk}/document/{filename}".format(
        pk=instance.pk, filename=filename
    )


class Contract(models.Model):
    """
    Модель контракта.
    Attributes:
        title (CharField): Название контракта.
        service (ForeignKey): Связь с orm моделью Product.
        document (FileField): Файл с документом.
        sum (DecimalField): Сумма контракта.
        start_date (DateTimeField): Начало действия контракта.
        end_date (DateTimeField): Конец действия контракта.
    """

    title = models.CharField(max_length=40, verbose_name="Название контракта")
    service = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="contracts",
        verbose_name="Услуга",
    )
    document = models.FileField(
        upload_to=contract_document_directory_path, verbose_name="Документ"
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Стоимость контракта",
    )
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Начало действия')
    end_date = models.DateTimeField(verbose_name='Конец действия')
    
    def __str__(self) -> str:
        return self.title
    
