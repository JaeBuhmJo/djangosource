from django.urls import path
from .views.base_views import (question_detail,index,)
from .views.question_views import (    
    question_create,
    question_edit,
    question_delete,
    vote_question,
    )
from .views.answer_views import (
    answer_create,
    answer_edit,
    answer_delete,
    vote_answer,
    )
from .views.comment_views import (
    comment_create_question,
    comment_edit_question,
    comment_delete_question,
    comment_create_answer,
    comment_edit_answer,
    comment_delete_answer,
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
    path("answer/delete/<int:aid>/", answer_delete, name="answer_delete"),

    path("comment/create/question/<int:qid>/", comment_create_question, name="comment_create_question"),
    path("comment/edit/question/<int:comment_id>/", comment_edit_question, name="comment_edit_question"),
    path("comment/delete/question/<int:comment_id>/", comment_delete_question, name="comment_delete_question"),
    path("comment/create/answer/<int:aid>/", comment_create_answer, name="comment_create_answer"),
    path("comment/edit/answer/<int:comment_id>/", comment_edit_answer, name="comment_edit_answer"),
    path("comment/delete/answer/<int:comment_id>/", comment_delete_answer, name="comment_delete_answer"),

    path("vote/question/<int:qid>/", vote_question, name="vote_question"),
    path("vote/answer/<int:aid>/", vote_answer, name="vote_answer"),
]
