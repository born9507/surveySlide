from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import random

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE) #유저가 탈퇴하면 누가 만든지는 삭제?
    total_reward = models.IntegerField(null=True)  
    isCompleted = models.BooleanField(default=False)
    # 제작 완료 됐는지를 알리는 요소가 필요함
    # 제작이 완료되지 않으면 설문조사가 배포되면 안되므로! 

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

    ##지우는 게 불가능하게 만들자. 중요한 데이터들이므로
    ##사용자가 설문을 지우면, 실제로는 지워지는 게 아니라 사용자에게 뜨지만 않도록 하자

class Question(models.Model):
    survey = models.ForeignKey(Survey, null=False, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500 ,blank=False, null=False)
    answered_users = models.ManyToManyField(User, blank=True, related_name='answer_question', through='Answer')

class Choice(models.Model):
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)

class Result(models.Model):
    interviewee = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, null=False, on_delete=models.CASCADE)
    content = models.TextField()

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, blank=True, null=True, on_delete=models.CASCADE)
    question =models.ForeignKey(Question,blank=True,null=True, on_delete=models.CASCADE)