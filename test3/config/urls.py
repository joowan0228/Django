from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),   # 관리자 페이지
    path("", include("todo.urls")),    # 루트 URL을 todo 앱에 연결
]
