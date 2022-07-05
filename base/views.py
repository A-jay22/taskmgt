from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm
from . models import Task, Activities
from . addtask import AddTask
from . addactivities import AddActivities

# Create your views here

activities = [
    {'id':1, 'name':'Write a list of the ingredients and foodstuff needed'},
    {'id':2, 'name':'Go to the market'},
    {'id':3, 'name':'Call my cousins over to help'},
    {'id':4, 'name':'Do the cooking on friday into saturday morning'},
]

def index(request):
    return render(request,'base/index.html')  

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'invalid username')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user.save()      
            return redirect('home')
        else:
            messages.error(request, 'invalid username OR password')
    context = {}
    return render(request, 'base/login.html', context)

def setup(request):
    setupform = UserCreationForm()
    if request.method=='POST':
        setupform=UserCreationForm(request.POST)  
        if setupform.is_valid():
            user=setupform.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request, user)
            return redirect ('home')
        else:
            messages.error(request, 'An error occurred during registration') 
    context = {'setupform':setupform}
    return render(request, 'base/setup.html', context)

def home(request):
    print(request.user.id)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    tasks = Task.objects.filter(title__icontains=q)
    tasks = Task.objects.filter(user=request.user.id)
    count = Task.objects.filter(complete=False).count()
    context = {'tasks': tasks,'count':count }
    return render(request, 'base/home.html', context)  

def task(request, pk):
    task = Task.objects.get(id=pk)
    activities = Activities.objects.filter(task = Task.objects.get(id=pk))
    context = {'task': task, 'activities':activities} 
    return render(request, 'base/task.html', context)


def updatetask(request, pk):
    task = Task.objects.get(id=pk)
    addtask = AddTask(instance=task)
    if request.method =='POST':
        task_title=request.POST.get('title')
        task_complete=request.POST.get('complete')
        task.save()
        return redirect('home')
    context = {'task':task, 'addtask':addtask}
    return render(request, 'base/addtasks.html', context)

def activities(request, pk):
    activities = Activities.objects.filter(task = Task.objects.get(id=pk))
    # context = {'activities':activities } 
    return render(request, 'base/task.html', activities)

@login_required(login_url='index')
def addactivities(request):
    addactivities = AddActivities()
    if request.method == 'POST':
        addactivities = AddActivities(request.POST)
        if addactivities.is_valid():
            addactivities.save()
            return redirect('home')    
    context = {'addactivities': addactivities, 'task':task}
    return render(request, 'base/addactivities.html', context)

@login_required(login_url='index')
def edittask(request, pk):
    task=Task.objects.get(id=pk)
    edittasks = AddTask()
    if request.method == 'POST':
        edittasks = AddTask(request.POST)
        if edittasks.is_valid:
            edittasks.save()
            return redirect('home')
    context = {'edittasks':edittasks}
    return render(request, 'base/edittask.html', context)

def editactivities(request, pk):
    activities=Activities.objects.all()
    editactivities = AddActivities()
    if request.method == 'POST':
        editactivities = AddActivities(request.POST)
        if editactivities.is_valid:
            editactivities.save()
            return redirect('task')
    context = {'editactivities':editactivities}
    return render(request, 'base/editactivities.html', context)

@login_required(login_url='index')
def addtasks(request):
    addtask = AddTask()
    if request.method == 'POST':
        addtask = AddTask(request.POST)
        if addtask.is_valid():
            addtask.save()
            return redirect('home')    
    context = {'addtask': addtask}
    return render(request, 'base/addtasks.html', context)

@login_required(login_url='index')
def deletetasks(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request,'base/deletetasks.html', {'obj':task})

def deleteactivities(request, pk):
    activities=Activities.objects.get()
    if request.method == 'POST':
        activities.delete()
        return redirect('task')
    return render(request,'base/deleteactivities.html', {'obj':task})

def logoutPage(request):
    return render(request, 'base/index.html')


