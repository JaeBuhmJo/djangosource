from django.shortcuts import render
from .models import Question

def index(request):
    question_list = Question.objects.order_by("-pub_date")
    return render(request, "polls/index.html",{"question_list": question_list})

def detail(request, question_id):
    pass

def results(request, question_id):
    pass

def vote(request, question_id):
    pass
