import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Buckets(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title