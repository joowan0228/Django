"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


# 기본 페이지
def index(request):
    return HttpResponse('<h1>hello</h1>')


# 도서 페이지 (리스트)
def book_list(request):
    book_text = ''
    for i in range(0, 10):
        book_text += f'book {i}<br>'
    return HttpResponse(book_text)


# 도서 상세 페이지
def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return HttpResponse(book_text)


# 언어 페이지 (동적)
def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.</h1>')


# 특정 언어 페이지 (python 고정)
def python(request):
    return HttpResponse('python 페이지 입니다.')


# 영화 페이지
def movies(request):
    return HttpResponse("<h1>영화 페이지입니다 🎬</h1>")


# 구구단 페이지
def gugudan(request, dan):
    result = ""
    for i in range(1, 10):
        result += f"{dan} x {i} = {dan * i}<br>"
    return HttpResponse(result)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    # 도서 관련
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),

    # 언어 관련
    path('language/<str:lang>/', language),
    path('language/python/', python),

    # 영화 페이지
    path('movies/', movies),

    # 구구단 페이지
    path('gugudan/<int:dan>/', gugudan),
]
