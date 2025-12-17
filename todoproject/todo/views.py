from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todo/detail.html', {'todo': todo})

def add_todo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo/add.html', {'form': form})
def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_detail', id=id)
    # Pass 'todo' to template to avoid NoReverseMatch
    return render(request, 'todo/edit.html', {'form': form, 'todo': todo})


def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/delete.html', {'todo': todo})
