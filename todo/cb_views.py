from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .models import Todo
from .forms import TodoForm, TodoUpdateForm

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    form_class = TodoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('cbv_todo_info', kwargs={'pk': self.object.id})

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    form_class = TodoUpdateForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise Http404("권한이 없습니다.")
        return obj

    def get_success_url(self):
        return reverse_lazy('cbv_todo_info', kwargs={'pk': self.object.id})
