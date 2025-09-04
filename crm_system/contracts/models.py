from django.db import models
from django.core.validators import MinValueValidator

from services.models import Service


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
        service (ForeignKey): Связь с orm моделью Service.
        document (FileField): Файл с документом.
        sum (DecimalField): Сумма контракта.
        created_at (DateTimeField): Начало действия контракта.
        contract_period (DateTimeField): Период действия контракта.
    """

    title = models.CharField(max_length=40)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    document = models.FileField(upload_to=contract_document_directory_path)
    sum = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    contract_period = models.DateTimeField()
