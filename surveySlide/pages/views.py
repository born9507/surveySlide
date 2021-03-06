from django.shortcuts import render, redirect
from pages.models import Survey, Question, Choice, Answer, Result
import random

def index(request):
    user = request.user
    if user.is_authenticated:
        grade = user.profile.grade
        gender = user.profile.gender
        questions = (Question.objects
            .filter(survey__is_completed=True)
            .exclude(survey__is_deleted=True)
            .exclude(answered_users=request.user)
            .exclude(survey__author=request.user)
            .exclude(choice=None)
            .filter(survey__grade_filter=grade)
            .filter(survey__gender_filter=gender)
        )
        numQuestions = questions.count()
        Answers = Answer.objects.all()
        reward = round(random.normalvariate(50,28))
        if numQuestions == 0:
            return render(request, 'pages/index.html', {'numQuestions': numQuestions, 'Answers': Answers})
        else:
            question = questions.order_by("?").first()  # 랜덤하게 배열해서 첫번째
            return render(request, 'pages/index.html', {'question': question, 'numQuestions': numQuestions, 'reward': reward, 'Answers': Answers})
    else:
        return render(request, 'pages/index.html')

def survey_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        explanation = request.POST['explanation']
        gender_filter = request.POST['gender_filter']
        grade_filter = request.POST['grade_filter']
        survey = (Survey(
            title=title, 
            author=request.user, 
            is_completed=False, 
            explanation=explanation, 
            gender_filter=gender_filter, 
            grade_filter=grade_filter
        ))
        survey.save()
        return render(request, 'pages/surveyUpdate.html', {'survey':survey}) #여기서 해당 설문조사의 아이디를 넘겨주어야 한다.
    return render(request, 'pages/surveyCreate.html')

def survey_read(request):
    user = request.user
    return render(request, 'pages/surveyRead.html', {'user':user})

def survey_update(request, sid):
    survey = Survey.objects.get(id=sid)
    survey.is_completed = False #수정 누르면 다시 '작성중'으로 바뀌도록
    survey.save()
    if request.method == 'POST':
        title = request.POST['title']
        survey.title = title
        survey.save()
        return render(request, 'pages/surveyUpdate.html', {'survey':survey})
    return render(request, 'pages/surveyUpdate.html', {'survey':survey})
        
def survey_expUpdate(request, sid):
    survey = Survey.objects.get(id=sid)
    explanation = request.POST['explanation']
    survey.explanation = explanation
    survey.save()
    return render(request, 'pages/surveyUpdate.html', {'survey':survey})
    

def survey_delete(request, sid):
    # 실제로 설문조사를 삭제하지 않고 설문 시행자와 설문지의 연결관계만 끊도록 함수 구현하기! (데이터는 남아있도록)
    survey = Survey.objects.get(id=sid)
    survey.is_deleted = True
    survey.save()
    return redirect('/show/')

def survey_complete(request, sid):
    survey = Survey.objects.get(id=sid)
    survey.is_completed = True
    survey.save()
    return redirect('/show/')

def question_create(request, sid):
    survey = Survey.objects.get(id=sid)
    question_text = request.POST['question_text']
    question = Question(survey_id=sid, question_text=question_text)
    question.save()
    return render(request, 'pages/surveyUpdate.html', {'survey':survey})

def question_update(request, sid, qid):
    survey = Survey.objects.get(id=sid)
    question = Question.objects.get(id=qid)
    question_text = request.POST['question_text']
    question.question_text = question_text
    question.save()
    return redirect('/edit/'+str(sid)+'/')
    # return render(request, 'pages/surveyUpdate.html', {'survey':survey})

def question_delete(request, sid, qid):
    survey = Survey.objects.get(id=sid)
    question = Question.objects.get(id=qid)
    question.delete()
    return redirect('/edit/'+str(sid)+'/')
    # return render(request, 'pages/surveyUpdate.html', {'survey':survey})

def choice_create(request, sid, qid):
    survey = Survey.objects.get(id=sid)
    question = Question.objects.get(id=qid)
    choice_text = request.POST['choice_text']
    choice = Choice(question_id=qid, choice_text=choice_text)
    choice.save()
    return render(request, 'pages/surveyUpdate.html', {'survey':survey, 'question':question})

def choice_update(request, sid, qid, cid):
    choice = Choice.objects.get(id=cid)
    choice_text = request.POST['choice_text']
    choice.choice_text = choice_text
    choice.save()
    return redirect('/edit/'+str(sid)+'/')
    # return render(request, 'pages/surveyUpdate.html', {'survey':survey, 'question':question})

def choice_delete(request, sid, qid, cid):
    choice = Choice.objects.get(id=cid)
    choice.delete()
    return redirect('/edit/'+str(sid)+'/')

def survey_results(request):
    surveys= Survey.objects.filter(is_completed=True).exclude(is_deleted=True).filter(author=request.user)
    return render(request, 'pages/surveyResults.html', {'surveys':surveys})

def survey_result(request, sid):
    survey=Survey.objects.get(id=sid)
    results = Result.objects.filter(interviewer=request.user).filter(survey=survey)
    return render(request, 'pages/surveyResult.html', {'survey':survey, 'results':results})

def price_policy(request):
    return render(request, 'pages/pricePolicy.html')

def service_intro(request):
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
    Answer.objects.create(user=request.user, question=question, choice=choice)

    return redirect('/')