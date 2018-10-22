from django.db import models


class Data(models.Model):
    seq = models.IntegerField(primary_key=True)
    keywords = models.CharField(max_length=128)
    entities = models.CharField(max_length=128)
    categories = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    source = models.CharField(max_length=128)
    etc = models.CharField(max_length=128)
# Create your models here.
    def __str__(self):
        return self.keywords
