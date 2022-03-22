from django.db import models

from ads.models import Ad
from users.models import User


class Selection(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"

    def __str__(self):
        return self.name

