from django.urls import path
from .views import index, question_detail, answer_create, question_create

app_name = "board"

urlpatterns = [
    path("",index, name="index"),
    path("<int:qid>/",question_detail, name="detail"),
    path("create/",question_create, name="question_create"),
    path("answer/create/<int:qid>/", answer_create, name="answer_create")
]
