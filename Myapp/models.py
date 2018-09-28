from django.db import models


class Data(models.Model):
    keywords = models.CharField(max_length=128, primary_key=True)
    concepts = models.CharField(max_length=128)
    entities = models.CharField(max_length=128)
    categories = models.CharField(max_length=128)
    source = models.CharField(max_length=128)
# Create your models here.
    def __str__(self):
        return self.keywords
