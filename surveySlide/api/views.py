from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Survey, Question, Choice, Result, Answer
from .serializers import UserSerializer, SurveySerializer
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class SurveyView(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
