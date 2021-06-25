from django.db import models
from company.models import Company
from devices.models import Device


# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Manager(models.Model):
    name = models.CharField(max_length=100, null=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Staff(models.Model):
    name = models.CharField(max_length=100, null=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)
