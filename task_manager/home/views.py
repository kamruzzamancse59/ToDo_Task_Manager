from django.shortcuts import render, HttpResponse, redirect
from home.models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db import models

# Create your views here.
def signuppage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password is not same!")
        
        else:
            print(username,email,pass1)
            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("User name or Password is incorrect")
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    context={ 'success':False}
    if request.method == "POST":
        # Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        due_date = request.POST['date']
        print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc, date_field=due_date)
        ins.save()
        context = { 'success':True}
    return render(request,'index.html', context)

@login_required(login_url='login')
def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request,'tasks.html',context)

@login_required(login_url='login')
def details(request,id):
    if request.method == "POST":    
        task = Task.objects.get(id=id)
        
       
    task=task = Task.objects.get(id=id)
    context={'id': task.id,'title': task.taskTitle, 'description': task.taskDesc, 'status':task.status,'date':task.date_field,'time':task.time}
    return render(request,'details.html',context)


@login_required(login_url='login')
def update(request,id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        id=id
        title = request.POST['title']
        desc = request.POST['desc']
        status= request.POST['status']
 
        due_date = request.POST['date']

        ins = Task(id=id,taskTitle=title, taskDesc=desc, date_field=due_date, time=task.time, status=status)
        ins.save()
        print("Updated")
        context = { 'success':True}
        return render(request,'update.html',context)
        
    task = Task.objects.get(id=id)

    context={'id': task.id,'title': task.taskTitle, 'description': task.taskDesc, 'status':task.status,'date':task.date_field}
    print(context)
    return render(request,'update.html',context)
    

    

@login_required(login_url='login')
def delete(request,id):
    if request.method == "POST":    
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('tasks')
    task=task = Task.objects.get(id=id)
    context={'id': task.id,'title': task.taskTitle, 'description': task.taskDesc, 'status':task.status,'date':task.date_field}
    return render(request,'delete.html',context)