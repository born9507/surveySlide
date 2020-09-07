from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions

from django.contrib.auth.models import User
from django.http import Http404

from .models import Survey, Question, Choice, Result, Answer
from .serializers import SurveySerializer, QuestionSerializer, ChoiceSerializer
import random

class SurveyList(generics.ListCreateAPIView):
    serializer_class = SurveySerializer

    # overrides get method
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            gender = user.profile.gender
            grade = user.profile.grade
            queryset = Survey.objects.filter(
                is_completed=True,
                is_closed=False,
                gender_filter=gender,
                grade_filter=grade
            ).exclude(
                author=user
            )
            return queryset
        else:
            print('no user')
            queryset = Survey.objects.all()   
            return queryset

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('invalid request')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


