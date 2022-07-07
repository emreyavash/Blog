from celery import shared_task,Celery,states
from celery.exceptions import Ignore

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notifications  
import asyncio
import json
@shared_task(bind=True)
def broadcast_notification(self,data):
    print(data)
    try:
        notification = Notifications.objects.filter(id = int(data))
        if len(notification)>0:
            notification = notification.first()
            channel_layer = get_channel_layer()
            loop=asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(channel_layer.group_send(
                "notification_broadcast",{
                    'type':'send_notification',
                    'message':json.dumps(notification.message),
                }
            ))
            notification.sent=True
            notification.save()
            return 'Done'
        else:
            self.update_state(
                state="FAILURE",
                meta = {'exe':'Not Found'}
            )
            raise Ignore()
    except:
        self.update_state(
                    state="FAILURE",
                    meta = {
                        'exe':'Failed',
                    }
                )
        raise Ignore()
            