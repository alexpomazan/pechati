from django.db import models
from django.core.urlresolvers import reverse

class Pechat(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='static/images/', blank=True)
    slug = models.SlugField(blank=True)

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


class Klishe(models.Model):
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='klishe_image/', blank=True)
    ip_or_ooo = (
        ('ip', 'ИП'),
        ('organisation', 'Организация'),
    )
    form = models.CharField(max_length=50, choices=ip_or_ooo, default='ip')

    def __str__(self):
        return str(self.id) + ' ' + self.form
