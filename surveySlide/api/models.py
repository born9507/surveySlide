from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import random

class Survey(models.Model):
    title = models.CharField(max_length=50)
    explanation = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE) # 유저가 탈퇴하면 누가 만든지는 삭제?
    total_reward = models.IntegerField(null=True)  
    is_completed = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    gender_filter = models.CharField(max_length=10, null=True) # 특정 성별 뿐 아니라 range로 묶으면 좋을 듯
    grade_filter = models.IntegerField(null=True) # 위와 마찬가지

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update_date(self):
        self.updated_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
        
class Question(models.Model):
    survey = models.ForeignKey(Survey, null=False, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500 ,blank=False, null=False)
    answered_users = models.ManyToManyField(User, blank=True, related_name='answer_question', through='Answer')

class Choice(models.Model):
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    chosen_users = models.ManyToManyField(User, blank=True, related_name='choose_choice', through='Answer')

class Result(models.Model):
    interviewer = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="interviewer")
    interviewee = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="interviewee")
    survey = models.ForeignKey(Survey, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, null=False, on_delete=models.CASCADE)
    content = models.TextField(null=True)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question =models.ForeignKey(Question,blank=True, null=True, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,blank=True, null=True, on_delete=models.CASCADE)

