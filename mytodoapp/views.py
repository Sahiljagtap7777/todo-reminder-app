from django.shortcuts import render,HttpResponse, get_object_or_404,redirect
from mytodoapp.models import Task
# Create your views here.


def mytodoapp(request):
    context = {'success': False,'name':'Sahil'}  # Default value for success

    if request.method == "POST":
        # Handle the form
        title = request.POST.get('title')  # Use get to avoid KeyError
        desc = request.POST.get('desc')
        print(title, desc)  # Debugging: Check if title and desc are being printed

        if title:  # Only save if title field is provided
            ins = Task(taskTitle=title, taskDesc=desc)
            ins.save()
            context = {'success': True}  # Update success to True


    return render(request, 'index.html', context)  # Pass context to the template
def task(request):
    allTasks= Task.objects.all()
    context ={'tasks':allTasks}
    return render(request,'task.html',context)

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task')  # Replace 'task' with the name of the view that renders the task list

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    
    if request.method == 'POST':  # If the form is submitted
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        
        if title and desc:  # Ensure both fields are filled
            task.taskTitle = title
            task.taskDesc = desc
            task.save()  # Save the updated task
            return redirect('task')  # Redirect to task list
    
    return render(request, 'update_task.html', {'task': task})  # Render the update form

def delete_all_tasks(request):
    if request.method == 'POST':
        Task.objects.all().delete()  # Delete all tasks from the database
        return redirect('task')  # Redirect to the task list page

    return redirect('task')  # Redirect to the task list if not a POST request
