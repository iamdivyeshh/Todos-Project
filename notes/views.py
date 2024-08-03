from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    context = {'page':'Home Page'}
    return render(request, 'homepage.html',context)

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/todos/')
        
    context = {'page':'Login Page'} 
    return render(request,'login.html',context)

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create (
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.error(request, 'Account created Successfully')
        return redirect('/register/')
    context = {'page':'Register'}  
    return render(request,'signup.html',context)
def logout_page(request):
    logout(request)
    return redirect('/login/')
@login_required(login_url="/login/")
def todos(request):
    if request.method == "POST":
        data = request.POST
        todo_name = data.get('todo_name')
        todo_description = data.get('todo_description')

        Todos.objects.create(
            todo_name = todo_name,
            todo_description = todo_description,
        )
        return redirect('/todos/')
    mydata = Todos.objects.all().order_by('todo_name').values()
    context = {
    'todos': mydata,
  }
    return render(request,'writenotes.html',context)

def delete_todo(request , id):
    queryset = Todos.objects.get(id = id)
    queryset.delete()
    return redirect('/todos/')

def update_todo(request,id):
    queryset = Todos.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        todo_name = data.get('todo_name')
        todo_description = data.get('todo_description')

        queryset.todo_name = todo_name
        queryset.todo_description = todo_description
        queryset.save()
        return redirect('/todos/')
    context = {"todos": queryset}
    return render (request,'update.html',context)

def view_todo(request):
    queryset = Todos.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(todo_name__icontains = request.GET.get('search'))
    context = {"todos": queryset}
    return render (request,'view_notes.html',context)

