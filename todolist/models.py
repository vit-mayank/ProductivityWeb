from django.db import models
from django.contrib.auth.models import User
from mycalendar.models import events
# Create your models here.
class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length = 240)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    def __str__ (self):
        return self.title
    
class Event_Todo(models.Model):
    event = models.ForeignKey(events,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.event.title