from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, TaskUpdate
from .models import Task
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def home(request):
    search_input = request.GET.get('search-area') if request.GET.get('search-area') != None else ''
    tasks = Task.objects.filter(
        Q(title__icontains=search_input) 
    )
    tasks = Task.objects.filter(user=request.user)
    count = tasks.filter(complete=False).count()

    context = {'tasks': tasks, "count": count, "search_input": search_input}
    return render(request, 'core/home.html', context)

@login_required(login_url='login')
def taskForm(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            nameHs = form.save(commit=False)
            nameHs.user = request.user
            nameHs.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'core/task-form.html', context)

def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskUpdate(instance=task)

    if request.method == 'POST':
        form = TaskUpdate(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'core/task-update.html', context)

def taskDelete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'core/task-delete.html', {'task': task})
