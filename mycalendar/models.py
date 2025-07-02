from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    

def get_default_category():
    return Category.objects.filter(title='Others').first().id

class events(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField(default=date.today)
    category = models.ForeignKey(Category,default=get_default_category, on_delete=models.SET_DEFAULT)
    def __str__(self):
        return self.title
    

