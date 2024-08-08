from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .models import Choice

def index(request):
    # questions= Question.objects.all()
    #return HttpResponse( Question.question_text for Question in questions)
    return render(request, 'polls/index.html')
def choice(request):
    choices= Choice.objects.all()
    return HttpResponse(Choice.choice_text for Choice in choices)