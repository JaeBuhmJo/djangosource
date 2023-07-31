from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import Question, Answer, Comment
from ..forms import CommentForm

from django.contrib.auth.decorators import login_required
from django.utils import timezone

#######질문 댓글
@login_required(login_url="users:login")
def comment_create_question(request, qid):
    question = get_object_or_404(Question, id=qid)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.question = question
            comment.save()
            # return redirect("board:detail", qid = qid)
            # name 앵커 이용
            return redirect("{}#comment_{}".format(resolve_url("board:detail",qid=qid), comment.id))

    else:
        form = CommentForm()

    return render(request, "board/comment_form.html",{"form":form})

@login_required(login_url="users:login")
def comment_edit_question(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            return redirect("{}#comment_{}".format(resolve_url("board:detail",qid=comment.question.id), comment.id))
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html",{"form":form})

@login_required(login_url="users:login")
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect("board:detail", qid = comment.question.id)

#######답변 댓글
@login_required(login_url="users:login")
def comment_create_answer(request, aid):
    answer = get_object_or_404(Answer, id=aid)
    qid = answer.question.id
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.answer = answer
            comment.save()
            # name 앵커 이용
            return redirect("{}#comment_{}".format(resolve_url("board:detail",qid=qid), comment.id))

    else:
        form = CommentForm()

    return render(request, "board/comment_form.html",{"form":form})

@login_required(login_url="users:login")
def comment_edit_answer(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            qid = comment.answer.question.id
            comment.modified_at = timezone.now()
            comment.save()
            return redirect("{}#comment_{}".format(resolve_url("board:detail",qid=qid), comment.id))
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html",{"form":form})

@login_required(login_url="users:login")
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    qid = comment.answer.question.id
    comment.delete()
    return redirect("board:detail", qid = qid)
