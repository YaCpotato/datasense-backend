from django.db import models

# Create your models here.

from django.utils import timezone


class DataInfo(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    columns = models.CharField(max_length=200)
    discription = models.TextField()
    created_at = models.DateTimeField(
            default=timezone.now)
    updated_at = models.DateTimeField(
            blank=True, null=True)
    deleted_at = models.DateTimeField(
            blank=True, null=True)