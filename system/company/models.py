from django.db import models
from django.contrib.auth.models import User
from devices.models import Device
from accounts.models import Membership


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    company_location = models.CharField(max_length=100, null=True) #recall to edit
    company_email = models.EmailField(max_length=80, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ManyToManyField(User)
    subscription = models.ForeignKey(Membership, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.company_name)