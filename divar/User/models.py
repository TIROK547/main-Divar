from django.db import models
import re
from django.core.validators import RegexValidator

def validate_iran_phone_number(phone_number):
    pattern = r'^\+98\d{10}$'
    return re.match(pattern, phone_number)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(regex=r'^\+98\d{10}$', message="Enter a valid Iranian phone number.")],
        unique=True
    )