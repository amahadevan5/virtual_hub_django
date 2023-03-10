from django.db import models
from django.urls import reverse

class County(models.Model):
    name = models.CharField(max_length=50)
    shape = models.PolygonField() # assuming the shape of the county is represented by a PolygonField

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('county-detail', kwargs={'pk': self.pk})
