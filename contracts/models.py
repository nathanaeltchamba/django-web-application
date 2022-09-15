from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Contract(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, unique=True, null=True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100, null=True)

    project_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150, null=True)
    description = models.TextField(max_length=250, null=True)
    project_length = models.CharField(max_length=100, null=True)
    contingencies = models.CharField(max_length=100, null=True)

    price = models.IntegerField()
    payment_schedule = models.CharField(max_length=100, null=True)
    permits = models.CharField(max_length=100, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # image =

    def __str__(self):
        return self.company_name
