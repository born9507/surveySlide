from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/login.cgi/', views.index, name='index'),

    path('serviceIntro/', views.service_intro),
    path('pricePolicy/', views.price_policy),

    path('new/', views.survey_create),
    path('new/<int:sid>/', views.question_create),
    path('new/<int:sid>/<int:qid>/', views.choice_create),
    
    path('show/', views.survey_read),

    path('edit/<int:sid>/', views.survey_update),
    path('edit/<int:sid>/explanation/', views.survey_expUpdate),
    path('edit/<int:sid>/<int:qid>/', views.question_update),
    path('edit/<int:sid>/<int:qid>/<int:cid>/', views.choice_update),

    path('delete/<int:sid>/', views.survey_delete),
    path('delete/<int:sid>/<int:qid>/', views.question_delete),
    path('delete/<int:sid>/<int:qid>/<int:cid>/', views.choice_delete),
    
    path('complete/<int:sid>/', views.survey_complete),
    
    path('answer/<int:cid>/<int:reward>', views.answer, name='answer'),

    path('result/', views.survey_results),
    path('result/<int:sid>/', views.survey_result),
]
