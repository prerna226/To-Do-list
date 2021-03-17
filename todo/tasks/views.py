from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    try:
        tasks = Task.objects.all()
        forms = TaskForm()
        
        if request.method == 'POST':
            forms = TaskForm(request.POST)
            if forms.is_valid():
                forms.save()
            return redirect('/') # return back to same url path

        context = {'tasks':tasks, 'forms':forms}
        return render(request, 'tasks/list.html',context)
    except Exception as e:
        return HttpResponse(str(e))

def update_task(request,pk):
    try:
        task = Task.objects.get(id=pk)
        form = TaskForm(instance= task)  # it will take the same task model and will prefilled the fields, if no instance will be given then it will be blank
        
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
            return redirect('/')
        
        context = {'form':form}
        return render(request,'tasks/update_task.html',context)
    except Exception as e:
        return HttpResponse(str(e))
    
def delete_task(request,pk):
    try:
        item = Task.objects.get(id=pk)
        
        if request.method == 'POST':
            item.delete()
            return redirect('/')
        
        context = {'item':item}
        return render(request, 'tasks/delete.html',context)
    except Exception as e:
        return HttpResponse(str(e))
