from django.db import models
from apps.data_models.models import DataModel, UserDataModel
from .utils import generate_otp
from django.utils import timezone
from datetime import timedelta
from django.conf import settings


class OTP(UserDataModel):
    code = models.CharField(max_length=64, blank=False, null=False, default=generate_otp, verbose_name="Code")

    @classmethod
    def is_expired(self):
        cond = self.created_at + timedelta(seconds=settings.OTP["life_time"]) < timezone.now()
        return cond
