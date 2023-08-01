from django.shortcuts import render, get_object_or_404
from ..models import Question, QuestionCount
from django.core.paginator import Paginator
from ..tools.utils import get_client_ip

from django.db.models import Q, Count

def index(request):
    page = request.GET.get('page',1)
    keyword = request.GET.get("keyword","")
    sort = request.GET.get("sort","recent")

    if sort =="recommend":
        question_list = Question.objects.annotate(num_voter = Count("voter")).order_by("-num_voter","-created_at")
    elif sort =="popular":
        question_list = Question.objects.annotate(num_answer = Count("answer")).order_by("-num_answer","-created_at")
    else:
        question_list = Question.objects.order_by("-created_at")

    if keyword:
        question_list = question_list.filter(
            Q(subject__icontains = keyword)|
            Q(content__icontains = keyword)|
            Q(author__username__icontains = keyword)|
            Q(answer__author__username__icontains = keyword)
        ).distinct()

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {"question_list": page_obj, "page":page, "keyword":keyword, "sort":sort}

    return render(request, "board/question_list.html", context)

def question_detail(request, qid):
    page = request.GET.get('page')
    keyword = request.GET.get("keyword")
    sort = request.GET.get("sort")

    question = get_object_or_404(Question, id=qid)
    
    # 조회수 증가
    # client ip 가져오기
    ip = get_client_ip(request)

    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:
        # QuestionCount 테이블에 ip와 question 추가
        qc = QuestionCount(ip=ip, question=question)
        qc.save()
        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1
        question.save()


    context = {
        "question":question,
        "page":page,
        "keyword":keyword,
        "sort":sort,
        }

    return render(request, "board/question_detail.html", context)

