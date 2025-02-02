from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        if "save" in response.POST:
            for item in ls.item_set.all():
                item.completed = response.POST.get("c" + str(item.id)) == "clicked"
                item.save()

        elif "newItem" in response.POST:
            txt = response.POST.get("new")
            if txt:
                ls.item_set.create(text=txt, completed=False)

        # return redirect('index', id=ls.id)  # Replace 'index' with your URL name

    return render(response, "main/list.html", {"ls": ls})


def all_lists(response):
    lists = ToDoList.objects.all()  # Fetch all To-Do lists
    return render(response, "main/all_lists.html", {"lists": lists})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        
            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def view(response):
    return render(response, "main/view.html", {})