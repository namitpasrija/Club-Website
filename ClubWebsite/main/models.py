from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    fname = models.CharField(max_length=100, blank=True)
    lname = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    batch = models.IntegerField(default=2017)
    facebook = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.fname

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Event(models.Model):
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=500)
    host = models.ManyToManyField(User)
    venue = models.CharField(max_length=100)
    fee = models.IntegerField(default=0)
    rules = models.TextField(blank=True, null=True)
    prerequistes = models.TextField(blank=True, null=True)
    start_date = models.DateField(default=datetime.date.today,auto_now=False,auto_now_add=False)
    end_date = models.DateField(default=datetime.date.today,auto_now=False,auto_now_add=False)
    start_time = models.TimeField(default=datetime.datetime.now().time(),auto_now=False,auto_now_add=False)
    end_time = models.TimeField(default=datetime.datetime.now().time(),auto_now=False,auto_now_add=False)
    def __str__(self):
        return self.title 

class registration(models.Model):
    eventid = models.IntegerField()
    mobile = models.CharField(max_length=20)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100,default="")
    College = models.CharField(max_length=300)
    email = models.EmailField()
    query = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.fname + str(self.eventid)

