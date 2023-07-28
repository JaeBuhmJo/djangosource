from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import NameForm, QuestionForm, AnswerForm
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
    page = request.GET.get('page',1)

    question_list = Question.objects.order_by("-created_at")

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj}

    return render(request, "board/question_list.html", context)

def question_detail(request, qid):

    question = get_object_or_404(Question, id=qid)
    context = {"question":question}

    return render(request, "board/question_detail.html", context)

@login_required(login_url="users:login")
def question_create(request):
    """
    질문등록
    get - 비어있는 QuestionForm 보내기
    post - QuestionForm에 사용자 입력값 연결
    """
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

#######답변
@login_required(login_url="users:login")
def answer_create(request, qid):

    # question = get_object_or_404(Question, id=qid)
    # question.answer_set.create(content=request.POST["content"])

    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect("board:detail", qid=qid)
    else:
        form = AnswerForm()
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)


def answer_edit(request, aid):
    answer = get_object_or_404(Answer, id=aid)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modified_at = timezone.now()
            answer.save()
            return redirect("board:detail", answer.question_id)
    else:
        form = AnswerForm(instance=answer)

    return render(request, "board/answer_edit.html", {"form":form})

def answer_delete(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    answer.delete()
    return redirect("board:detail", answer.question_id)
