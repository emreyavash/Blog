from django.contrib import admin
from .models import Notifications,NotificationChannel,NotificationTypes
# Register your models here.
admin.site.register(Notifications)
admin.site.register(NotificationChannel)
admin.site.register(NotificationTypes)
