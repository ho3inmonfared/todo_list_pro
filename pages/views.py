from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task, Category

def home(request):
    tasks = Task.objects.order_by('-created_at')
    categories = Category.objects.all()

    # add task 
    if request.method == 'POST' and 'add_task' in request.POST:
        text = request.POST.get('text')
        category_id = request.POST.get('category')
        if text and category_id:
            Task.objects.create(text=text, category_id=category_id)
        return redirect('home')

    #complete task or not 
    if request.method == 'POST' and 'toggle_task' in request.POST:
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.is_complete = not task.is_complete
        task.save()
        return redirect('home')

    # delete
    if request.method == 'POST' and 'delete_task' in request.POST:
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('home')

    # stats
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(is_complete=True).count()
    pending_tasks = total_tasks - completed_tasks

    return render(request, 'pages/home.html', {
        'tasks': tasks,
        'categories': categories,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks
    })
