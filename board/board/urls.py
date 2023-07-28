from django.urls import path
from .views import (
    index,
    question_detail,
    answer_create,
    question_create,
    question_edit,
    question_delete,
    answer_edit,
    answer_delete
    )

app_name = "board"

urlpatterns = [
    path("",index, name="index"),
    path("<int:qid>/",question_detail, name="detail"),
    path("question/create/",question_create, name="question_create"),
    path("question/modify/<int:qid>/",question_edit, name="question_modify"),
    path("question/delete/<int:qid>/",question_delete, name="question_delete"),
    path("answer/create/<int:qid>/", answer_create, name="answer_create"),
    path("answer/modify/<int:aid>/", answer_edit, name="answer_modify"),
    path("answer/delete/<int:aid>/", answer_delete, name="answer_delete")
]
