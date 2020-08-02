from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=50)
    # author = models.ForeignKey(User, null=False, on_delete=models.CASCADE) #유저가 탈퇴하면 누가 만든지는 삭제?
    # total_reward = models.IntegerField()

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

class Choice(models.Model):
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)

class Result(models.Model):
    interviewee = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, null=False, on_delete=models.CASCADE)
    content = models.TextField()