from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
    
def new(request):
    return render(request, 'pages/new.html')

def surveyMake(request):
    title = request.POST['title']
    Survey.object.create(title=title)
    return render(request, 'pages/new.html')

# def questionMake(request):
#     qtext = request.POST['title']
#     return render(request, 'pages/new.html')
