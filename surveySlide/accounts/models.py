from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=20, blank=True, null=True)
    grade=models.IntegerField(null=True)
    gender=models.CharField(max_length=20, null=True)
    point = models.IntegerField(default=1000)
    changedpoint = models.IntegerField(default=0)
    chargedpoint = models.IntegerField(default=0)
    gainedpoint= models.IntegerField(default=0)

    def __str__(self):
        return f'id={self.id}, user_id={self.user.id}, college={self.college}, major={self.major}, point={self.point}, changedpoint={self.changedpoint}'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()
