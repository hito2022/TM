from django.shortcuts import render
from index import forms
import datetime
from index.models import student
# Create your views here.
new_time = 0 
finish_time = 0

def record(request):
    record = student.objects.order_by("name")
    dict = {"record":record}
    return render(request,'record.html' , context = dict)
def time_record(request):
    global new_time
    new_time = datetime.datetime.now()
    dict = {"new_time":new_time}
    return render(request,'time.html' , context = dict)

def finish(request):
    global new_time
    finish_time = datetime.datetime.now()
    total_time = finish_time - new_time
    total_time = str(total_time)
    dict = {"finish_time":finish_time,"new_time":new_time, "total_time":total_time }
    return render(request,'finish.html' , context = dict)

def start(request):
    student_form = forms.studentForm()
    dict = {"student_form": student_form}
    if request.method == "POST": 
        student_form = forms.studentForm(request.POST)
        if student_form.is_valid():
            student_form.save(commit =True)
            return time_record(request)
    return render(request,'start.html' , context = dict)
