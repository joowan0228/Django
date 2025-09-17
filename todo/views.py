from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Todo
from .forms import TodoForm, TodoUpdateForm

@login_required
def todo_list(request):
    qs = Todo.objects.filter(user=request.user).order_by('-created_at')
    q = request.GET.get('q', '').strip()
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
    page_num = request.GET.get('page', 1)
    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(page_num)
    return render(request, 'todo/todo_list.html', {'page_obj': page_obj, 'q': q})

@login_required
def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    return render(request, 'todo/todo_info.html', {'todo': todo.__dict__, 'todo_obj': todo})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo:todo_info', todo_id=todo.id)
    else:
        form = TodoForm()
    return render(request, 'todo/todo_create.html', {'form': form})

@login_required
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_info', todo_id=todo.id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form, 'todo': todo})

@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})
