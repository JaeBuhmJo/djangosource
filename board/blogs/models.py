from django.db import models
from django.contrib.auth.models import User

# 테이블 생성
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="작성자")
    subject = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, verbose_name="이미지")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    # auto_now : update시 매번 변경
    modified_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    
    def __str__(self) -> str:
        return self.subject
