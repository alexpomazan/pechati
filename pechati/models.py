from django.db import models


class Pechat(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='static/images/', blank=True)

    def __str__(self):
        return self.name


class Osnastka(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=4, decimal_places=0, default=0)
    image = models.ImageField(upload_to='static/images/', blank=True)

    def __str__(self):
        return self.title
