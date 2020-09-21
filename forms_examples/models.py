from django.db import models

# Create your models here.

class SimpleTable(models.Model):
    char_collumn = models.CharField(max_length=30)
    int_collumn = models.IntegerField()
    float_collumn = models.FloatField()
    text_collumn = models.TextField(max_length=1000)
