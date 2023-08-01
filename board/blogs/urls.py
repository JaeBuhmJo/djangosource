from django.urls import path
from .views import post_list,post_create,post_edit,post_delete, post_detail, post_like

app_name = 'blog'

urlpatterns = [
    path("", post_list, name="post_list"),
    path("create/", post_create, name="post_create"),
    path("detail/<int:post_id>", post_detail, name="post_detail"),
    path("edit/<int:post_id>", post_edit, name="post_edit"),
    path("delete/<int:post_id>", post_delete, name="post_delete"),
    path("likes/<int:post_id>", post_like, name="post_like"),
]
