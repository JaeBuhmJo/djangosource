from .models import Question, Answer, Comment
from django import forms

class NameForm(forms.Form):
    # 화면에 보여줄 요소
    name = forms.CharField(
        label="name", max_length=100, error_messages={"required":"이름입력"}
    )

class QuestionForm (forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]
    
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]