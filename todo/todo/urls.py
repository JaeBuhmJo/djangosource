
from django.urls import path
from . import views

urlpatterns = [
    path("",views.todo_list,name = "todo_list"),
    path("<int:id>/",views.todo_detail,name = "todo_detail"),
    path("new/",views.todo_create,name = "todo_create"),
    path("<int:id>/edit/",views.todo_edit,name = "todo_edit"),
    path("done/<int:id>/",views.todo_done,name = "todo_done"),
    path("done/",views.done_list,name = "done_list"),
]