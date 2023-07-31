from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import Question, Answer
from ..forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

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
            # detail 앵커 이용
            return redirect("{}#answer_{}".format(resolve_url("board:detail",qid=qid), answer.id))
    else:
        form = AnswerForm()
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)

@login_required(login_url="users:login")
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

@login_required(login_url="users:login")
def answer_delete(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    answer.delete()
    return redirect("board:detail", answer.question_id)

@login_required(login_url="users:login")
def vote_answer(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    qid = answer.question.id
    if answer.author==request.user:
        messages.error(request, "본인이 작성한 댓글은 추천할 수 없습니다.")
    else:
        answer.voter.add(request.user)
    return redirect("board:detail", qid=qid)
