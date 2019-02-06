from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class PhoneNumber(models.Model):
    country = models.CharField(max_length = 1)
    area = models.CharField(max_length = 3)
    phone_number = models.CharField(max_length = 7)
    reg_date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('country', 'area', 'phone_number')

    def add_to_database(self):
        self.save()

    def __str__(self):
        return str(self.country) + str(self.area) + str(self.phone_number)
