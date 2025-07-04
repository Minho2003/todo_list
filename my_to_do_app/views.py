from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

# 문자열을 화면에 출력
'''
def index(request):
    return HttpResponse("니의 To Do List")
'''

def index(request):
    todos= ToDo.objects.all()
    content={ 'todos' : todos }
    return render(request, 'my_to_do_app/simple_page.html',content)

def createTodo(request):
    if request.method == 'POST':
        new_todo= request.POST['memo']
        todo= ToDo(content=new_todo)
        todo.save()
        return redirect('index')
    else: return HttpResponse("잘못된 요청입니다.")

def deleteTodo(request):
    if request.method == 'POST':
        todo_id = request.POST['todo_id']
        todo = ToDo.objects.get(id=todo_id)

        # Trash 최대 3개까지
        if Trash.objects.count() < 3:
            Trash.objects.create(content=todo.content)

        todo.delete()
        return redirect('index')
    else:
        return HttpResponse("잘못된 요청입니다.")

def updateTodo(request):
    if request.method == 'POST':
        new_todo = request.POST['memo']
        todo_id = request.POST['todo_id']
        todo = ToDo.objects.get(id=todo_id)
        todo.content = new_todo
        todo.save()
        return redirect('index')
    else:
        return HttpResponse("잘못된 요청입니다.")