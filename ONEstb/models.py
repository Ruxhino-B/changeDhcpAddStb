from django.db import models

# Create your models here.

class ONE_STB(models.Model):
    mac = models.CharField(max_length=17)

    def __str__(self):
        return self.mac