from django.db import models

# Create your models here.
from django.utils import timezone


class MusicalWork(models.Model):
    title = models.CharField(max_length=200,  blank=True, default='')
    contributors = models.TextField()
    iswc = models.CharField(max_length=100, unique=True, db_index=True)
    source = models.CharField(max_length=50, blank=True, default='')
    item_id = models.BigIntegerField(default=-1)

    batch = models.CharField(max_length=50, default='', blank=True)

    created_on = models.DateTimeField()
    modified_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-iswc', )

    def __str__(self):
        return self.iswc
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_on = timezone.now()
        super(MusicalWork, self).save(*args, **kwargs)