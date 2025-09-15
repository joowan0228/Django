from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:todo_id>/', views.todo_info, name='todo_info'),
]
