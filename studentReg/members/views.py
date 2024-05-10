from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Student
from django.contrib import messages
from django.urls import reverse

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({},request))

def show(request):
    mymembers = Student.objects.all().values()
    template = loader.get_template('show.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def addRecord(request):
    name = request.POST['name']
    age = request.POST['age']
    course = request.POST['course']
    address = request.POST['address']
    member = Student(name=name,age=age,address=address,course=course)

    if name=="" or age=="" or course=="" or address=="":
        messages.error(request,'Opps..! Somthing missing')
        return redirect('register')
    
    else:
        messages.success(request,"Student Register successfully..!!")
        member.save()
    return render(request,'register.html')
    

def delete(request,id):
    member = Student.objects.get(id=id)
    member.delete()
    messages.success(request,"Student Deleted successfully..!!")
    return HttpResponseRedirect(reverse('show'))

def update(request,id):
    mymember = Student.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    name = request.POST['name']
    age = request.POST['age']
    course = request.POST['course']
    address = request.POST['address']
    member = Student.objects.get(id=id)
    if name=="" or age=="" or course=="" or address=="":
        return redirect('show')
    else:
        member.name = name
        member.age = age
        member.course = course
        member.address = address
        member.save()
    return HttpResponseRedirect(reverse('show'))