
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class User(AbstractUser):
    pass


number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message='Le numéro doit contenir exactement 8 chiffres.'
)


def birth_date_validator(date):
    if date > timezone.now().date():
        raise ValidationError(
            "La date de naissance doit être antérieure à aujourd'hui."
        )


class Specialty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Doctor(User):
    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[
            RegexValidator(r'^\d{6}$',
                           'Le matricule doit contenir 6 chiffres.')
        ]
    )

    phone = models.CharField(
        max_length=8,
        unique=True,
        validators=[number_validator]
    )

    specialties = models.ManyToManyField(Specialty)

    def __str__(self):
        return self.username


class Patient(User):
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[number_validator]
    )

    phone = models.CharField(
        max_length=8,
        unique=True,
        validators=[number_validator]
    )

    birth_date = models.DateField(
        validators=[birth_date_validator]
    )

    def __str__(self):
        return self.username
