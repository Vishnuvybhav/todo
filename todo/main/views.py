from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import logout


def home(request):
    tasks = Task.objects.all() 

    form = taskform()
    if request.method == 'POST':
        form = taskform(request.POST)
        if form.is_valid():
           form.save()
        return redirect('/')   
    
    context = {'tasks':tasks,'form':form}
    return render(request,'list.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')

def update_task(request,pk):
    task = Task.objects.get(id=pk)
    form = taskform(instance=task)
    if request.method == 'POST':
        form = taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'update.html',context)

def delete_task(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'delete.html',context) 