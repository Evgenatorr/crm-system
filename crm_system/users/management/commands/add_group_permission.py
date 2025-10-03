from typing import Any
from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType
from advertising_companies.models import Advertising
from customers.models import ActiveClient
from leads.models import PotentialClient
from products.models import Product
from contracts.models import Contract


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        groups_config = {
            "Marketer": {
                "models": [Advertising, Product],
                "permissions": ["add", "change", "delete", "view"],
            },
            "Manager": {
                "models": [ActiveClient, Contract],
                "permissions": ["add", "change", "delete", "view"],
            },
            "Operator": {
                "models": [PotentialClient],
                "permissions": ["add", "change", "delete", "view"],
            },
        }

        for group_name, config in groups_config.items():
            group, created = Group.objects.get_or_create(name=group_name)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Создана группа: {group_name}"))
                for model in config["models"]:
                    content_type = ContentType.objects.get_for_model(model)

                    for permission_code in config["permissions"]:
                        codename = f"{permission_code}_{model._meta.model_name}"

                        try:
                            permission = Permission.objects.get(
                                codename=codename, content_type=content_type
                            )
                            group.permissions.add(permission)
                            self.stdout.write(f"Добавлено разрешение: {codename}")
                        except Permission.DoesNotExist:
                            self.stdout.write(
                                self.style.ERROR(f"Разрешение не найдено: {codename}")
                            )
                manager_group = Group.objects.get(name='Manager')
                permission = Permission.objects.get(codename='view_potentialclient')
                manager_group.permissions.add(permission)
            else:
                self.stdout.write(
                    self.style.WARNING(f"Группа уже существует: {group_name}")
                )

        self.stdout.write(self.style.SUCCESS("Настройка групп завершена!"))
