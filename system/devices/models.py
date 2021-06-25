from django.db import models


# Create your models here.
class Device(models.Model):
    device_name = models.CharField(max_length=200, null=True, blank=True)
    device_location = models.CharField(max_length=200, null=True, blank=True)  # location field re-examine
    timestamp = models.DateField(auto_now_add=True, null=True, blank=True)
    temperature = models.DecimalField(max_digits=8, decimal_places=2)
    humidity = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.device_name)
