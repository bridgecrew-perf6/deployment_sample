from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import OTP


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class OTPModelSerializer(ModelSerializer):
    class Meta:
        model = OTP
        fields = "__all__"