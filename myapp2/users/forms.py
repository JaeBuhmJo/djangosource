from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    # email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        # fields = "__all__"
        fields = ["username","email"] # + 상속받은(password1, password2)