import random
from django.conf import settings


def generate_otp():
    the_set = "1234567890"
    return "".join([random.choice(the_set) for _ in range(0, settings.OTP["length"])])


def issue_otp(user):
    from .models import OTP
    otp = OTP.objects.create(user=user)
    return otp
