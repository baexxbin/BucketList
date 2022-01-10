import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=10)
    id = models.CharField(max_length=20,primary_key=True)
    pw = models.CharField(max_length=20)
    point = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    
    def __str__(self):
        return self.id

CATEGORY = (
    ('wantDo','wantDo'),
    ('wantHave','wantHave')
)
class Buckets(models.Model):
    bk_idx = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="",blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY)
    created_at = models.DateTimeField(auto_now_add=True)
    target_at = models.DateTimeField()
    completed_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey("Member", related_name="owner", on_delete=models.CASCADE, db_column="owner")
    
    def __str__(self):
        return self.title