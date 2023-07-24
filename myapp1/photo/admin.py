from django.contrib import admin
from .models import Photo
# admin에서 관리할 모델 정보 / admin 환경 설정
# admin 사용하기 위해서는 admin 계정 생성 필요
# python manage.py createsuperuser

# admin에서 CRUD 가능케함
admin.site.register(Photo)
