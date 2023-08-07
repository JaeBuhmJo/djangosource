from django.urls import path, include
from .views import TodosApiView

urlpatterns = [
    path('', TodosApiView.as_view(), name="todo"),
]
