from django.shortcuts import render, get_object_or_404
from ..models import Question, Answer, Comment
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

