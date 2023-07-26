from django.shortcuts import render, get_object_or_404, redirect
from .models import Question

def index(request):
    question_list = Question.objects.order_by("-pub_date")
    return render(request, "polls/index.html",{"question_list": question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    return render(request, "polls/detail.html", {"question":question})

def results(request, question_id):
    question = get_object_or_404(Question,id=question_id)
    return render(request, "polls/results.html", {"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question,id=question_id)
    if request.method == "POST":
        try:
            selected_choice = question.choice_set.get(id=request.POST["choice"])
        except KeyError as e:
            return render(request, "polls/detail.html")
        else:
            selected_choice.vote += 1
            selected_choice.save()
            return redirect("results", question_id = question_id)