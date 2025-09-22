from django.urls import path
from . import cb_views

app_name = "todo"

urlpatterns = [
    path("cb/", cb_views.TodoListView.as_view(), name="cb_list"),
    path("cb/<int:pk>/", cb_views.TodoDetailView.as_view(), name="cb_detail"),
    path("cb/create/", cb_views.TodoCreateView.as_view(), name="cb_create"),
    path("cb/<int:pk>/update/", cb_views.TodoUpdateView.as_view(), name="cb_update"),
    path("cb/<int:pk>/delete/", cb_views.TodoDeleteView.as_view(), name="cb_delete"),

    path('comment/<int:todo_id>/create/', cb_views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', cb_views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', cb_views.CommentDeleteView.as_view(), name='comment_delete'),

]
