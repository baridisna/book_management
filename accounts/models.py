from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    role = models.ForeignKey(
        'Role',
        to_field='slug',
        default='member',
        on_delete=models.PROTECT
    )


class Role(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
