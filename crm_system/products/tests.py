import logging
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

logger = logging.getLogger(__name__)

User = get_user_model()


class ProductCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_superuser(
            username="test_superuser", email="test@example.com", password="testpass"
        )
        logger.info("Создан тестовый суперпользователь для Product тестова")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.user.delete()
        logger.info("Удалён тестовый суперпользователь после выполнения тестов")

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_create_product(self):
        logger.debug("Выполнение теста test_create_product")
        response = self.client.post(
            reverse("products:products-create"),
            {
                "price": 10000,
                "title": "test_product",
                "description": "test_description",
            },
        )
        self.assertRedirects(response, reverse("products:products-list"))
        logger.info("Тест test_create_product успешно выполнен")
