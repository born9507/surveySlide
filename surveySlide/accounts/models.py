from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=20, blank=True, null=True)
    grade = models.IntegerField(null=True)
    gender = models.CharField(max_length=20, null=True)
    point = models.IntegerField(default=1000)
    changed_point = models.IntegerField(default=0)
    charged_point = models.IntegerField(default=0)
    gained_point = models.IntegerField(default=0)

    def __str__(self):
        return f'id={self.id}, user_id={self.user.id}, college={self.college}, major={self.major}, point={self.point}, changed_point={self.changed_point}'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance)
        print('user created')

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()
    print('user saved')
