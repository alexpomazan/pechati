from django.db import models

class Pechat(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
