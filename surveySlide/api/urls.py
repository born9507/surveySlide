from django.urls import include, path
from . import views

from django.contrib import admin

urlpatterns = [
    path('', views.SurveyList.as_view()),
    path('new/', views.SurveyList.as_view()),
    path('new/<int:sid>/', views.QuestionList.as_view()),
    path('new/<int:sid>/<int:qid>', views.ChoiceList.as_view()),
]
