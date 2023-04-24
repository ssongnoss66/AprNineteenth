# AprNineteenth

django-admin startproject 프로젝트명 .

## 프로젝트
### urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ...,
    path('accounts/', include('accounts.urls'))
]

## accounts
### urls.py
app_name = 'accounts' (app_name임 appname 아니고 + app_name에서 accounts 지정했으면 urlpatterns 주소에서 accounts/안 씀)
urlpatterns = [
    path('login/', views.login, name='login'),
    ...,
]

### models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

### forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

### views.py
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required