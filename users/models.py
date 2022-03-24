from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


min_user_age = 9


def check_age(value: int):
    if value < min_user_age:
        raise ValidationError(f"{value} less than 9", params={'value': value})


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):
    member = "member"
    moderator = "moderator"
    admin = "admin"
    ROLES = [
        (member, "Пользователь"),
        (moderator, "Модератор"),
        (admin, "Админ"),
    ]

    role = models.CharField(max_length=10, choices=ROLES, default="member")
    age = models.PositiveSmallIntegerField(validators=[check_age])
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(null=True)
    email = models.CharField(max_length=100, unique=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username

