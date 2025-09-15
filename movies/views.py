from django.shortcuts import render
from django.http import HttpResponse

def movie_list(request):
    return HttpResponse("<h1>🎬 영화 페이지</h1><p>여기에 영화 목록이 표시됩니다.</p>")
