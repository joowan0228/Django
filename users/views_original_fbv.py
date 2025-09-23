from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as django_login

# 회원가입
def sign_up(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)  # 로그인 페이지로 이동

    return render(request, 'registration/signup.html', {'form': form})

# 로그인
def login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())
        return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'registration/login.html', {'form': form})
