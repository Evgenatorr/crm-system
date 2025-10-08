from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self) -> bool | None:
        user = self.request.user
        return user.is_superuser


class ManagerRequiredMixin(BaseMixin):
    """
    Mixin для прав менеджера
    """
    
    def test_func(self) -> bool | None:
        return super().test_func() or self.request.user.groups.filter(name="Manager").exists()


class MarketerRequiredMixin(BaseMixin):
    """
    Mixin для прав маркетолога
    """
    
    def test_func(self) -> bool | None:
        return super().test_func() or self.request.user.groups.filter(name="Marketer").exists()


class OperatorRequiredMixin(BaseMixin):
    """
    Mixin для прав оператора
    """
    
    def test_func(self) -> bool | None:
        return super().test_func() or self.request.user.groups.filter(name="Operator").exists()
