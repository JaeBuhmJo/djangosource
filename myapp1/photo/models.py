from django.db import models

"""
photo 앱에서 사용할 테이블 정의
클래스로 정의 - ORM(클래스 == 테이블)
python manage.py makemigrations(class파일 => sql 코드로 변환)
python manage.py migrate (sql 코드 변환 => 테이블 생성)
"""

class Photo(models.Model):
    """
    create table photo ~~
    """
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    