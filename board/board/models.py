from django.db import models
from django.contrib.auth.models import User

# Question, Answer 모델에서 author, voter 두 개의 필드가 User 모델 참조
# user.question_set 이렇게 Question 모델에 접근할 때 어느 필드가 기준이냐?

# Question table
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_question")
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)
    voter = models.ManyToManyField(User, related_name="voter_question")
    view_cnt = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.subject
    
# Answer table
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="author_answer")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)
    voter = models.ManyToManyField(User, related_name="voter_answer")

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="댓글내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)

class QuestionCount(models.Model):
    """
    조회수 업데이트를 위한 모델
    사용자의 ip 저장
    """
    ip = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ip