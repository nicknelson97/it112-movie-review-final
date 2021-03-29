from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    mtitle=models.CharField(max_length=255)
    mdate=models.DateField()
    mrating=models.CharField(max_length=10)
    mreview=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.mtitle

    class Meta:
        db_table='movie' 

