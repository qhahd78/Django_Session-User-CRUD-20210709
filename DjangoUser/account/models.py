from django.db import models
# 기본 유저의 필드들을 유지한채로 새로운 필드를 추가하기. 
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser) : 
    nickname = models.CharField(max_length=50)
    university = models.CharField(max_length=50)