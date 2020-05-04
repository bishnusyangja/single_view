from django.db import models

# Create your models here.


class MusicalWork(models.Model):
    title = models.CharField(max_length=200,  blank=True, default='')
    contributers = models.TextField()
    iswc = models.CharField(max_length=100, unique=True)
    source = models.CharField(max_length=50, blank=True, default='')
    item_id = models.BigIntegerField(default=-1)