from django.shortcuts import render, redirect
from pages.models import Survey, Question, Choice

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def surveyCreate(request):
    if request.method == 'POST':
        title = request.POST['title']
        survey = Survey(title=title, author=request.user)
        survey.save()
        return render(request, 'pages/surveyCreate.html', {'survey':survey}) #여기서 해당 설문조사의 아이디를 넘겨주어야 한다.
    return render(request, 'pages/surveyCreate.html')

def surveyDelete():
    # 이건 실제로 설문조사를 삭제하지 않고 설문 시행자와 설문지의 연결관계만 끊도록!!
    # 함수 구현
    return redirect('/result/')

def surveyUpdate():
    return render(request, 'pages/surveyUpdate.html')


def questionCreate(request, sid):
    survey = Survey.objects.get(id=sid)
    question_text = request.POST['question_text']
    question = Question(survey_id=sid, question_text=question_text)
    question.save()
    return render(request, 'pages/surveyCreate.html', {'survey':survey})

def choiceCreate(request, sid, qid):
    survey = Survey.objects.get(id=sid)
    question = Question.objects.get(id=qid)
    choice_text = request.POST['choice_text']
    choice = Choice(question_id=qid, choice_text=choice_text)
    choice.save()
    return render(request, 'pages/surveyCreate.html', {'survey':survey, 'question':question})

def result(request):
    user = request.user
    return render(request, 'pages/surveyResult.html', {'user':user})


def pricePolicy(request):
    return render(request, 'pages/pricePolicy.html')

def serviceIntro(request):
    return render(request, 'pages/serviceIntro.html')