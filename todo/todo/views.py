from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):

    # 전체 목록 가져오기
    # todos = Todo.objects.all()

    # 미완료된 목록 가져오기
    # where complete = 0
    todos = Todo.objects.filter(complete = False)
    
    return render(request, "todo/todo_list.html", {"todos":todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request,"todo/todo_detail.html",{"todo":todo})

def todo_create(request):
    """
    get / post 둘 다 동작
    """
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect("todo_detail", id=todo.id)
    else:
        form = TodoForm()

    return render(request, "todo/todo_create.html", {"form":form})

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            todo=form.save()
            return redirect("todo_detail", id=todo.id)
    else:
        form = TodoForm(instance=todo)

    return render(request, "todo/todo_edit.html", {"form":form})

def todo_done(request, id):
    # todo = get_object_or_404(Todo,id=id)
    todo = Todo.objects.get(id=id)
    todo.complete = True
    todo.save()
    
    return redirect("todo_list")

def done_list(request):
    dones = Todo.objects.filter(complete = True)
    
    return render(request, "todo/done_list.html", {"dones":dones})