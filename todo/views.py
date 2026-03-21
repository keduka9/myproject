from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # 追加
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import TaskForm
from django.utils import timezone # 追加

@login_required     # このデコレータを追加するだけ
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        # title = request.POST.get('title')
        if form.is_valid():
            task = form.save(commit=False)  # まだDBに保存しない
            task.user = request.user        # ユーザーを紐づける
            task.save()
        return redirect('index')

    # 優先度順 → 期限順 で並び替え
    priority_order = {'high': 0, 'medium': 1, 'low': 2}
    tasks = Task.objects.filter(user=request.user).order_by('done', 'due_date')
    form = TaskForm()
    today = timezone.now().date()   # 追加
    return render(request, 'todo/index.html', {
        'tasks': tasks,
        'form': form,
        'today': today,     # 追加
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def delete_task(request, task_id):
    # 自分のタスクでなければ404を返す
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
    return redirect('index')

@login_required
def toggle_task(request, task_id):
    # 完了・未完了の切り替え
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.done = not task.done
        task.save()
    return redirect('index')