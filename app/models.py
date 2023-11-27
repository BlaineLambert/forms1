from django.db import models

class Input(models.Model):
    first = models.CharField(max_length=100)
    second = models.CharField(max_length=100)

