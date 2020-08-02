from django.shortcuts import render
from pages.models import Survey, Question, Choice

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
    
def new(request):
    return render(request, 'pages/new.html')

def surveyCreate(request):
    title = request.POST['title']
    survey = Survey(title=title)
    survey.save()
    return render(request, 'pages/new.html', {'survey':survey}) #여기서 해당 설문조사의 아이디를 넘겨주어야 한다.

# def surveyDelete():
# def surveyUpdate():
# def surveyRead(): 굳이 필요 없으려나?

def questionCreate(request, sid):
    survey = Survey.objects.get(id=sid)
    question_text = request.POST['question_text']
    question = Question(survey_id=id, question_text=question_text)
    question.save()
    return render(request, 'pages/new.html', {'survey':survey})

def choiceCreate(request, sid, qid):
    survey = Survey.objects.get(id=sid)
    question = Question.objects.get(id=qid)
    choice_text = request.POST['choice_text']
    choice = Choice(question_id=qid, choice_text=choice_text)
    return render(request, 'pages/new.html', {'survey':survey, 'question':question})
