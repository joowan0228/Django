from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "todos"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Todo.objects.all().order_by("-created_at")
        return Todo.objects.filter(user=self.request.user).order_by("-created_at")

class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = "todo/todo_info.html"
    context_object_name = "todo"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Todo.objects.all()
        return Todo.objects.filter(user=self.request.user)

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = "todo/todo_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("todo:cb_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = "todo/todo_form.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("todo:cb_list")

    def get_queryset(self):
        if self.request.user.is_staff:
            return Todo.objects.all()
        return Todo.objects.filter(user=self.request.user)

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = "todo/todo_confirm_delete.html"
    success_url = reverse_lazy("todo:cb_list")

    def get_queryset(self):
        if self.request.user.is_staff:
            return Todo.objects.all()
        return Todo.objects.filter(user=self.request.user)
