from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    address = models.CharField(max_length=250)
    is_published = models.BooleanField(default=False)
    #image = models.ImageField(upload_to="ads_image/", null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


