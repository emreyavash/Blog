from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()