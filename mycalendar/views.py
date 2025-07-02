from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from calendar import HTMLCalendar
from .models import events
from todolist.models import Event_Todo
from .forms import EventCreationForm
from datetime import datetime
# Create your views here.

class myHTMLCalendar(HTMLCalendar):
    def __init__(self,firstweekday,data):
        super().__init__(firstweekday=firstweekday)
        self.data=data

    def formatday(self,day,weekday):
        temp = super().formatday(day=day,weekday=weekday)
        if day == datetime.now().day:
            temp = temp.replace('td ','td id="today"')
        if day in self.data:
            toreplace = str(day)
            replacewith = "" + str(day)
            for i in self.data[day]:
                replacewith  += '''<a href="'''+ reverse('update_event',args=(i.id,))+'''"><div style="background-color:'''+ i.category.color +'''">''' + str(i.title) + '''</div></a>'''
            temp = temp.replace(toreplace,replacewith)
        return temp
    def formatmonthname(self, theyear, themonth, withyear = True):
        return super().formatmonthname(theyear, themonth, withyear).replace('<th colspan="7" class="month">','''<th colspan="7" class="month"><button class="btn btn-primary float-start mx-5" type="submit" form="prev">Prev</button><button class="btn btn-primary float-end mx-5" type="submit" form="next">Next</button>
        <a class="btn btn-success" href="'''+ reverse('create_event')+'''">Add</a>
        ''')
    cssclass_month = "month w-100"

@login_required
def mycalendar(request):
    if request.method == "POST":
        year = int(request.POST.get("year"))
        month = int(request.POST.get("month"))
        action = request.POST.get("action")
        if action=="+":
            if month==12:
                month = 1
                year+=1
            else:
                month += 1
        else:
            if month==1:
                month=12
                year -=1
            else:
                month-=1
    else:
        year = datetime.now().year
        month =datetime.now().month
    data1 = events.objects.filter(user=request.user)
    data={}
    for i in data1:
        if (i.event_date.year == year and i.event_date.month==month) or (str(i.category) == "Birthday" and i.event_date.month == month):
            if i.event_date.day in data:
                data[i.event_date.day]+=[i,]
            else:
                data[i.event_date.day] = [i,]
    cal = myHTMLCalendar(firstweekday=6,data=data).formatmonth(year,month)
    return render(request,"mycalendar/index.html",{'cal':cal,'year':year,'month':month})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            if str(form.category)!="Others":
                event_todo = Event_Todo(event = form)
                event_todo.save()
            return redirect('mycalendar')
    else:
        form = EventCreationForm()
    return render(request,'mycalendar/create.html',{'form':form,'data': None})

@login_required
def update_event(request,eventid):
    data = get_object_or_404(events,user=request.user,pk=eventid)
    if request.method == "POST":
        form = EventCreationForm(request.POST,instance=data)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('mycalendar')
    else:
        form = EventCreationForm(instance=data)
        return render(request,'mycalendar/create.html',{'form':form,'data':data})

@login_required  
def delete_event(request,eventid):
    data = get_object_or_404(events, user=request.user,pk=eventid)
    if request.method=="POST":
        data.delete()
        return redirect('mycalendar')
    return render(request,'mycalendar/delete.html',{'data':data})
