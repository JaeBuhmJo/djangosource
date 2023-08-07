from django.db import models

class Todo(models.Model):
    """
    제목, 설명, 작성날짜, 완료여부, 중요여부
    """
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
