from django.shortcuts import render, redirect
from .forms import UserForm

# 장고에서 제공하는 User 생성폼과 모델 가져오기
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

# 비밀번호 변경
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def index(request):
    return render(request,"index.html")

def user_main(request):
    return render(request, "users/main.html")

# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("users:login")
#     else:
#         form = UserCreationForm()

#     return render(request, "users/register.html", {"form":form})
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = UserForm()

    return render(request, "users/register.html", {"form":form})

def common_login(request):
    """
    개발자가 login 직접 구현시
    직접 구현하지 않고 장고에서 제공하는 LoginView 이용할 수 있음
    """

    if request.method == "POST":
        # 사용자 입력값 가져오기
        username = request.POST["username"]
        password = request.POST["password"]
        # 사용자가 존재한다면 권한을 가진 user 객체를 리턴해줌
        user = authenticate(request, username = username, password = password)

        if user is not None:
            # 세션에 정보가 담기게 됨
            login(request, user)
            return redirect("index")

    return render(request, "users/login.html")

def common_logout(request):
    """
    개발자가 logout 직접 구현 시
    직접 구현하지 않고 장고가 제공하는 LogoutView 사용 가능
    """
    logout(request)
    return redirect("index")

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "users/password_change.html"
    success_url = reverse_lazy("users:login")

def common_password_change(request):
    """
    개발자가 직접 비밀번호 변경 구현 시
    """
    if request.method =="POST":
        form= PasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = PasswordChangeForm()

    return render(request, "users/password_change.html", {"form": form})