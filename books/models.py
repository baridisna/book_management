from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, blank=True, unique=True)
    description = models.TextField()
    author = models.CharField(max_length=200, blank=True)
    cover = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to='images/')
    created_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE
    )
