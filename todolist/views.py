from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Event_Todo
from .forms import Todolist_form, UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from datetime import datetime,timedelta
from django.db.models import Q


# Create your views here.
def Todolist_home(request):
    return render(request, "todolist/home.html")
@login_required
def List_Todolist(request):
    lists = TodoList.objects.filter(user = request.user)
    eventlist = Event_Todo.objects.filter(Q(event__user = request.user) & (Q(event__event_date = str((datetime.now()+timedelta(days=1)).date())) | Q(event__event_date = str(datetime.now().date())) | (Q(event__category__title = "Birthday") & Q(event__event_date__month = datetime.now().month) & (Q(event__event_date__day = (datetime.now()+timedelta(days=1)).day) | Q(event__event_date__day = datetime.now().day)))))
    ctx = {'lists': lists,'events':eventlist,'date':datetime.now().date}
    return render(request, 'todolist/list.html', ctx)

@login_required
def Create_Todolist(request):
    if request.method == "POST":
        form = Todolist_form(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
        return redirect('List_Todolist')
    else:
        form = Todolist_form()
    return render(request, 'todolist/create.html',{'form':form})

@login_required
def Edit_Todolist(request,Todolist_id):
    inst = get_object_or_404(TodoList,pk=Todolist_id, user = request.user)
    if request.method == "POST":
        form = Todolist_form(request.POST,instance=inst)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
        return redirect('List_Todolist')
    else:
        form = Todolist_form(instance=inst)
    return render(request,'todolist/create.html',{'form':form})

@login_required
def Delete_Todolist(request, Todolist_id):
    inst = get_object_or_404(TodoList, pk = Todolist_id, user = request.user)
    if request.method == "POST":
        inst.delete()
        return redirect('List_Todolist')
    return render(request,'todolist/delete.html',{"inst":inst})

        
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.set_password(form.cleaned_data['password1'])
            temp.save()
            login(request,temp)
            return redirect('List_Todolist')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html',{'form':form})

def completed(request,Todo_id):
    inst = get_object_or_404(TodoList,pk=Todo_id,user = request.user)
    inst.completed = not inst.completed
    inst.save()
    return redirect('List_Todolist')
def Event_completed(request,id):
    inst = get_object_or_404(Event_Todo,pk = id,event__user = request.user)
    inst.completed = not inst.completed
    inst.save()
    return redirect('List_Todolist')

