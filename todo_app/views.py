from django.shortcuts import render
from django.http import HttpResponseRedirect
from todo_app.models import Todo

# Create your views here.
def todo_list(request):
    todos=Todo.objects.all()
    return render(request,'todo_apphome.html',{"todos":todos})


def todo_delete(request,id):
    todos=Todo.objects.get(id=id)
    todos.delete()
    return HttpResponseRedirect("/")


def todo_create(request):
    if request.method=="GET":
        return render(request,"todo_appcreate.html")
    else:
        Todo.objects.create(title=request.POST['title'])
        return HttpResponseRedirect("/")
    
    
def todo_update(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=="GET":
        return render(request,"todo_appupdate.html",{"todo":todo})
    else:
        todo.title=request.POST["title"]
        todo.save()
        return HttpResponseRedirect("/")

