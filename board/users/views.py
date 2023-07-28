from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import UserForm
"""
django가 제공하는 users 테이블 사용
"""


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username = username, password = password)

            if user is not None:
                # 세션에 정보가 담기게 됨
                login(request, user)
                return redirect("index")

    else:
        form = UserForm()
    return render(request, "users/register.html", {"form":form})