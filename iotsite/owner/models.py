from django.db import models

# Create your models here.
class Position(models.Model):
    plate_id = models.CharField(max_length = 10)
    longitude = models.CharField(max_length = 20)
    latitude = models.CharField(max_length = 20)
    speed = models.IntegerField(default = 0)
 
    def __str__(self):
        return self.plate_id
