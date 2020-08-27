from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<int:id>/change_profile/', views.change_profile, name='change_profile'),
    path('<int:id>/profile/', views.profile, name='profile'),
    path('<int:id>/charge/', views.charge, name='charge'),
    path('<int:id>/change/', views.change, name='change'),
    
    path('firstsetting1/', views.firstsetting1, name='firstsetting1'),
    path('firstsetting2/', views.firstsetting2, name='firstsetting2'),
    path('firstsetting3/', views.firstsetting3, name='firstsetting3'),
    path('firstsetting4/', views.firstsetting4, name='firstsetting4'),
]