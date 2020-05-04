from django.db import models

# Create your models here.


class MusicalWork(models.Model):
    title = models.CharField(max_length=200)
    contributers = models.TextField(max_length=200)
    iswc = models.CharField(max_length=100)
    source = models.CharField(max_length=50)
    item_id = models.BigIntegerField()