import imp
from django.db import models
from Writer.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver 
from Bloglar.models import BlogComment
# Create your models here.
class NotificationTypes(models.Model):
    name= models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    
class Notifications(models.Model):
    room = models.CharField(max_length=50,blank=True)
    sender_user = models.ForeignKey(CustomUser,related_name="sender_user",on_delete=models.CASCADE)
    receiver_user =models.ForeignKey(CustomUser,related_name="receiver_user",on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    message_date = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
    class Meta:
        ordering = ('message_date',)
   

class NotificationChannel(models.Model):
    room = models.CharField(max_length=50,blank=True)
    sender_user = models.ForeignKey(CustomUser,related_name='sender1',on_delete=models.CASCADE,null=True)
    receiver_user = models.ForeignKey(CustomUser,related_name='receiver1',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.room

