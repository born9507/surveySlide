from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE) #유저가 탈퇴하면 누가 만든지는 삭제?
    total_reward = models.IntegerField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

# class Question(models.Model):
    

# class Choice(models.Model):

# class Result(models.Model):