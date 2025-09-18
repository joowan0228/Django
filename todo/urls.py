from django.urls import path
from . import cb_views

app_name = "todo"

urlpatterns = [
    path("cb/", cb_views.TodoListView.as_view(), name="cb_list"),
    path("cb/<int:pk>/", cb_views.TodoDetailView.as_view(), name="cb_detail"),
    path("cb/create/", cb_views.TodoCreateView.as_view(), name="cb_create"),
    path("cb/<int:pk>/update/", cb_views.TodoUpdateView.as_view(), name="cb_update"),
    path("cb/<int:pk>/delete/", cb_views.TodoDeleteView.as_view(), name="cb_delete"),
]
