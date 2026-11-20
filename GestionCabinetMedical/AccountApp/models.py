from django.db import models
from django.contrib.auth import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.utils import timezone
# Create your models here.
class User (AbstractUser):
    pass

number_validator = RegexValidator(r'^\d{8}$', 'Phone number must be entered in the format: "01XXXXXXXX".')
def birth_date_validator(date):
    if date > timezone.now().localdate():
        raise ValidationError("la date de naissance doit etre anterieure a la date d'aujourd'hui")
    return date

class Doctor (User) :
    license_number=models.CharField( max_length=6, unique=True,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    phone=models.CharField(max_length=8,unique=True,validators=[RegexValidator(number_validator)])



class Patient(User) :
    national_id=models.CharField(max_length=8,unique=True,validators=[RegexValidator(number_validator)])
    phone=models.CharField(max_length=8,unique=True,validators=[RegexValidator(number_validator)])
    birth_date=models.DateField(blank=True, validators=[birth_date_validator])

class Specialty :
    name=models.CharField(max_length=50)
    