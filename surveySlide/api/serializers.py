from rest_framework import serializers
from .models import Survey, Question, Choice, Result, Answer
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')

class SurveySerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)

    class Meta:
        model = Survey
        fields = (
            'title',
            'explanation',
            'author',
            'total_reward',
            'is_completed',
            'is_closed',
            'gender_filter',
            'grade_filter',
        )
        read_only_fields = ('created_at', 'updated_at') # instead of 'read_only=True'

    
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'