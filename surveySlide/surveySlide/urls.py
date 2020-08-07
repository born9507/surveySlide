"""surveySlide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import pages.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.views.index, name='index'),


    path('serviceIntro/', pages.views.serviceIntro),
    path('pricePolicy/', pages.views.pricePolicy),

    path('new/', pages.views.surveyCreate),
    path('new/<int:sid>/', pages.views.questionCreate),
    path('new/<int:sid>/<int:qid>/', pages.views.choiceCreate),
    
    path('show/', pages.views.surveyRead),

    path('edit/<int:sid>/', pages.views.surveyUpdate),
    path('edit/<int:sid>/explanation/', pages.views.surveyExpUpdate),
    path('edit/<int:sid>/<int:qid>/', pages.views.questionUpdate),
    path('edit/<int:sid>/<int:qid>/<int:cid>/', pages.views.choiceUpdate),

    path('delete/<int:sid>/', pages.views.surveyDelete),
    path('delete/<int:sid>/<int:qid>/', pages.views.questionDelete),
    path('delete/<int:sid>/<int:qid>/<int:cid>/', pages.views.choiceDelete),
    
    path('complete/<int:sid>/', pages.views.surveyComplete),

    
    path('answer/<int:cid>/<int:reward>', pages.views.answer, name='answer'),

    path('result/', pages.views.surveyResults),
    path('result/<int:sid>/', pages.views.surveyResult),

    path('account/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('account/signup/',accounts.views.signup, name='signup'),
    path('account/<int:id>/changeinfo/',accounts.views.changeinfo,name='changeinfo'),
    path('account/<int:id>/myinfo/',accounts.views.myinfo,name='myinfo'),
    path('account/<int:id>/charge/',accounts.views.charge, name='charge'),
    path('account/<int:id>/change/',accounts.views.change, name='change'),
    
    path('account/firstsetting1/', accounts.views.firstsetting1, name='firstsetting1'),
    path('account/firstsetting2/', accounts.views.firstsetting2, name='firstsetting2'),
    path('account/firstsetting3/', accounts.views.firstsetting3, name='firstsetting3'),
    path('account/firstsetting4/', accounts.views.firstsetting4, name='firstsetting4'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
