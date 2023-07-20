from django.db import models

class DataEntry(models.Model):
    intensity = models.IntegerField()
    likelihood = models.IntegerField()
    relevance = models.IntegerField()
    country = models.CharField(max_length=100)
    topics = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    end_year = models.CharField(max_length=4, blank=True)
    start_year = models.CharField(max_length=4, blank=True)
    insight = models.CharField(max_length=255)
    url = models.URLField()
    impact = models.CharField(max_length=255, blank=True)
    added = models.DateTimeField(null=True, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=255)