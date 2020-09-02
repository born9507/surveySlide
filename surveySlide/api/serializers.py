from rest_framework import serializers
from .models import Survey, Question, Choice, Result, Answer
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class SurveySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Survey
        fields = (
            'title',
            'explanation',
            'author',
            'total_reward',
            'is_completed',
            'is_deleted',
            'gender_filter',
            'grade_filter',
        )
        read_only_fields = ('created_at',)