from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.CharField(max_length = 50 ,primary_key=True, unique=True)
    password = models.CharField(max_length = 20)
    USER_TYPE_CHOICES = (
      (1, 'admin'),
      (2, 'police'),
      (3, 'owner'),
      (4, 'vendor'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.id

