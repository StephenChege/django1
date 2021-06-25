from django.db import models


# Create your models here.
class Membership(models.Model):
    OPTIONS = (
        ('Basic', 'Basic'),
        ('Professional', 'Professional'),
        ('Enterprise', 'Enterprise'),
    )

    membership_option = models.CharField(max_length=200, null=True, choices=OPTIONS)
