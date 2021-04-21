from django.db import models

# Create your models here.
class Appointment(models.Model):
    std_id = models.CharField(max_length=200)
    std_name = models.CharField(max_length=200)
    std_age = models.IntegerField()
    std_city = models.CharField(max_length=500)
    std_email = models.CharField(max_length=500)
    std_contact = models.CharField(max_length=500)
    std_dob = models.CharField(max_length=500)