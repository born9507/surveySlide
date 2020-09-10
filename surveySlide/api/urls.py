from django.urls import include, path
from . import views

from django.contrib import admin

# /api로 들어오는 요청

urlpatterns = [
    path('', views.SurveyList.as_view()),
]
