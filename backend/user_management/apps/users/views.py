from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .models import OTP
from rest_framework.permissions import AllowAny
from .serializers import UserModelSerializer, OTPModelSerializer


class UserModelViewset(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.filter(is_active=True)
    permission_classes = [AllowAny]


class OtpModelViewset(ModelViewSet):
    serializer_class = OTPModelSerializer
    queryset = OTP.objects.filter(is_active=True)
    permission_classes = [AllowAny]