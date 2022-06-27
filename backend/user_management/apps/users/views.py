from rest_framework.viewsets import ModelViewset
from django.contrib.auth.models import User
from .models import OTP
from rest_framework.permissions import AllowAny


class UserModelViewset(ModelViewset):
    query = User.objects.filter(is_active=True)
    permission_classes = [AllowAny]


class OtpModelViewset(ModelViewset):
    query = OTP.objects.filter(is_active=True)
    permission_classes = [AllowAny]