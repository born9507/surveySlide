from django.shortcuts import render, redirect
from pages.models import Survey, Question, Choice, Answer, Result
import random

# Create your views here.
def index(request):
    user=request.user
    if user.is_authenticated:
        questions = (Question.objects
            .filter(survey__isCompleted=True)
            .exclude(survey__isDeleted=True)
            .exclude(answered_users=request.user)
            .exclude(survey__author=request.user)
            .exclude(choice=None)
        )
        numQuestions = questions.count()
        Answers = Answer.objects.all()
        reward=round(random.normalvariate(50,28))
        if numQuestions == 0:
            return render(request, 'pages/index.html', {'numQuestions':numQuestions, 'Answers':Answers})
        else:
            question = questions.order_by("?").first()  #랜덤하게 배열해서 첫번째
            return render(request, 'pages/index.html', {'question':question, 'numQuestions':numQuestions,'reward':reward, 'Answers':Answers})
    else:
        return render(request, 'pages/index.html')

def surveyCreate(request):
    if request.method == 'POST':
        title = request.POST['title']
        explanation=request.POST['explanation']
        survey = Survey(title=title, author=request.user, isCompleted=False, explanation=explanation)
        survey.save()
        return render(request, 'pages/surveyUpdate.html', {'survey':survey}) #여기서 해당 설문조사의 아이디를 넘겨주어야 한다.
    return render(request, 'pages/surveyCreate.html')

def surveyRead(request):
    user = request.user
    return render(request, 'pages/surveyRead.html', {'user':user})

def surveyUpdate(request, sid):
    survey = Survey.objects.get(id=sid)
    survey.isCompleted = False #수정 누르면 다시 '작성중'으로 바뀌도록
    survey.save()
    if request.method == 'POST':
        title = request.POST['title']
        survey.title = title
        survey.save()
        return render(request, 'pages/surveyUpdate.html', {'survey':survey})
    return render(request, 'pages/surveyUpdate.html', {'survey':survey})
        
def surveyExpUpdate(request, sid):
    survey = Survey.objects.get(id=sid)
    explanation = request.POST['explanation']
    survey.explanation = explanation
    survey.save()
    return render(request, 'pages/surveyUpdate.html', {'survey':survey})
    

def surveyDelete(request, sid):
    # 나중에 이건 실제로 설문조사를 삭제하지 않고 설문 시행자와 설문지의 연결관계만 끊도록 함수 구현하기! (데이터는 남아있도록)
    survey = Survey.objects.get(id=sid)
    survey.isDeleted = True
    survey.save()
    return redirect('/show/')

def surveyComplete(request, sid):
    survey = Survey.objects.get(id=sid)
    survey.isCompleted = True
    survey.save()
    return redirect('/show/')

def questionCreate(request, sid):
    survey = Survey.objects.get(id=sid)
    question_text = request.POST['question_text']
    question = Question(survey_id=sid, question_text=question_text)
    question.save()
    return render(request, 'pages/surveyUpdate.html', {'survey':survey})

def questionUpdate(request, sid, qid):
    survey = Survey.objects.get(id=sid)
    question = Question.objects.get(id=qid)
    question_text = request.POST['question_text']
    question.question_text = question_text
    question.save()
    return redirect('/edit/'+str(sid)+'/')
    # return render(request, 'pages/surveyUpdate.html', {'survey':survey})

def questionDelete(request, sid, qid):
    survey = Survey.objects.get(id=sid)
    question = Question.objects.get(id=qid)
    question.delete()
    return redirect('/edit/'+str(sid)+'/')
    # return render(request, 'pages/surveyUpdate.html', {'survey':survey})

def choiceCreate(request, sid, qid):
    survey = Survey.objects.get(id=sid)
    question = Question.objects.get(id=qid)
    choice_text = request.POST['choice_text']
    choice = Choice(question_id=qid, choice_text=choice_text)
    choice.save()
    return render(request, 'pages/surveyUpdate.html', {'survey':survey, 'question':question})

def choiceUpdate(request, sid, qid, cid):
    choice = Choice.objects.get(id=cid)
    choice_text = request.POST['choice_text']
    choice.choice_text = choice_text
    choice.save()
    return redirect('/edit/'+str(sid)+'/')
    # return render(request, 'pages/surveyUpdate.html', {'survey':survey, 'question':question})

def choiceDelete(request, sid, qid, cid):
    choice = Choice.objects.get(id=cid)
    choice.delete()
    return redirect('/edit/'+str(sid)+'/')

def surveyResult(request):
    user = request.user
    return render(request, 'pages/surveyUpdate.html', {'user':user})


def pricePolicy(request):
    return render(request, 'pages/pricePolicy.html')

def serviceIntro(request):
    return render(request, 'pages/serviceIntro.html')

def answer(request, cid, reward):
    interviewee = request.user
    choice = Choice.objects.get(id=cid)
    question = choice.question
    survey = question.survey
    interviewer = survey.author
    choice_text = choice.choice_text

    request.user.profile.point=request.user.profile.point+reward
    request.user.profile.gainedpoint=request.user.profile.gainedpoint+reward
    request.user.profile.save()
    
    Result.objects.create(interviewer=interviewer, interviewee=interviewee, survey=survey, question=question, choice=choice, content=choice_text)
    Answer.objects.create(user=request.user, question=question)

    return redirect('/')