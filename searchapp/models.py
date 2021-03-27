from django.db import models
from datetime import datetime

class Musician(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    city = models.CharField(max_length=50)
    user_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    yearly_income = models.IntegerField()
    description = models.TextField()
    list_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
    
