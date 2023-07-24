from django.urls import path
from . import views

urlpatterns = [
    # path(경로, 경로에 응답하는 함수, 함수 이름)
    path("",views.photo_list, name="photo_list"),
    # http://127.0.0.1:8000/photo/1
    path("<int:id>/",views.photo_detail, name="photo_detail"),
    # http://127.0.0.1:8000/photo/new + get
    path("new/",views.photo_post, name="photo_post"),
    # http://127.0.0.1:8000/photo/1/edit
    path("<int:id>/edit/",views.photo_edit, name="photo_edit"),
    # http://127.0.0.1:8000/photo/1/remove
    path("<int:id>/remove/",views.photo_remove, name="photo_remove"),
]
