from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question
from ..forms import QuestionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

#######질문
@login_required(login_url="users:login")
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect("board:index")
    else:
        form = QuestionForm()

    return render(request, "board/question_create.html",{"form":form})

@login_required(login_url="users:login")
def question_edit(request, qid):
    question = get_object_or_404(Question, id=qid)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modified_at = timezone.now()
            question.save()
            return redirect("board:detail", qid)
        
    else:
        form = QuestionForm(instance=question)

    return render(request, "board/question_edit.html" , {"form":form})

@login_required(login_url="users:login")
def question_delete(request, qid):
    question = get_object_or_404(Question, id=qid)
    question.delete()
    return redirect("board:index")

@login_required(login_url="users:login")
def vote_question(request, qid):
    question = get_object_or_404(Question, id=qid)
    if question.author==request.user:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        question.voter.add(request.user)
    return redirect("board:detail", qid=qid)
