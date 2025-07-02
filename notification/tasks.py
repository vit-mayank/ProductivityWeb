from webpush import send_user_notification
from todolist.models import Event_Todo
from webpush.models import PushInformation
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from django.db.models import Q

def send_reminder():
    subscribers = PushInformation.objects.all()
    for subscriber in subscribers:
        reminders = Event_Todo.objects.filter(Q(event__user = subscriber.user) & (Q(event__event_date = str((datetime.now()+timedelta(days=1)).date())) | Q(event__event_date = str(datetime.now().date())) | (Q(event__category__title = "Birthday") & Q(event__event_date__month = datetime.now().month) & (Q(event__event_date__day = (datetime.now()+timedelta(days=1)).day) | Q(event__event_date__day = datetime.now().day)))))
        for reminder in reminders:
            payload = {"head":reminder.event.title,"body":reminder.event.desc}
            send_user_notification(user=reminder.event.user, payload = payload, ttl=1000)
            
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_reminder,'cron',hour = 9, minute = 0)
    scheduler.start()