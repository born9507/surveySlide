from django.db import models
from django.utils import timezone

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, null=False) #유저가 탈퇴해도 설문지는 남아있도록
    total_reward = models.IntegerField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Question(models.Model):
    

class Choice(models.Model):

class Result(models.Model):