from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User
from django.http import Http404
from .models import Survey, Question, Choice, Result, Answer
from .serializers import UserSerializer, SurveySerializer, QuestionSerializer, ChoiceSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated, ]

class SurveyList(APIView):
    def get(self, request, format=None):
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SurveyDetail(APIView):
    def get_object(self, pk):
        try:
            return Survey.objects.get(pk=pk)
        except Survey.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class QuestionList(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChoiceList(APIView):
    def get(self, request, format=None):
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
