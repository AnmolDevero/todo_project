from django.shortcuts import render,redirect
# Create your views here.
from .models import Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Show all tasks
@login_required
def task_list(request):
    # Only fetch tasks that belong to the logged-in user
    tasks = Task.objects.filter (user = request.user).order_by('created_at')

    query = request.GET.get('query')
    if query:
        tasks = tasks.filter(title__icontains=query)

    paginator = Paginator(tasks,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render (request, 'task_list.html', {'tasks':page_obj})
    
# Add a new task
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']    
        # Use .get() to avoid error if 'description' is missing; default to ''                 
        description = request.POST.get('description','')
        # Save task with the current user
        Task.objects.create(title=title, description=description, user = request.user)
        return redirect ('task_list')
    return render(request, 'add_task.html')

# Delete task
@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')


# Toggle task completion
@login_required
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    # Flip the is_completed value (True ⇄ False) 
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task_list')

# Edit an existing task
@login_required
def edit_task(request, task_id):
    # Get task for the current user or show 404 if not found
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description','')
        task.save()
        return redirect('task_list')
    return render(request, 'edit_task.html', {'task':task})

# Sign up a new user
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserCreationForm()
    return render(request, 'sign_up.html', {'form':form})

 
@login_required
def delete_acount(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('signup')
    return render (request, 'delete_acount.html')

