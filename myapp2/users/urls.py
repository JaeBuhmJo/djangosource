from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("", views.user_main, name="main"),
    path("register/", views.signup, name="register"),
    # path("login/", views.common_login, name="login"),
    # path("logout/", views.common_logout, name="logout"),

    # 장고가 제공하는 views 사용하기
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/", views.CustomPasswordChangeView.as_view(), name="password_change"),
]

