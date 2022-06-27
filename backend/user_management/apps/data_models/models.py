from django.db import models
from django.contrib.auth.models import User


class DataModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    is_active = models.BooleanField(default=True, verbose_name="Is active")

    class Meta:
        abstract = True


class UserDataModel(DataModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")

    class Meta:
        abstract = True
