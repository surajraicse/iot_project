from django.db import models

class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'admin'),
      (2, 'police'),
      (3, 'owner'),
      (4, 'vendor'),
  )
  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
