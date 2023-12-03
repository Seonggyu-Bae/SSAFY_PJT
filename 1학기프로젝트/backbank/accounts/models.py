from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    nickname = models.CharField(max_length=255, blank=True, null=True, unique=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True)


