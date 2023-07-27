from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import NameForm, QuestionForm, AnswerForm
from django.core.paginator import Paginator


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

def question_create(request):
    """
    질문등록
    get - 비어있는 QuestionForm 보내기
    post - QuestionForm에 사용자 입력값 연결
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("board:index")
    else:
        form = QuestionForm()

    return render(request, "board/question_create.html",{"form":form})

def question_edit(request, qid):
    pass

def question_delete(request, qid):
    pass

#######답변
def answer_create(request, qid):

    # question = get_object_or_404(Question, id=qid)
    # question.answer_set.create(content=request.POST["content"])

    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("board:detail", qid=qid)
    else:
        form = AnswerForm()
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)


def answer_edit(request, aid):
    pass

def answer_delete(request, aid):
    pass
