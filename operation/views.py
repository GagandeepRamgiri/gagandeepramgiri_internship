from django.shortcuts import render, redirect
from .models import crud
from django.core.mail import send_mail
from qrcode import *

# Create your views here.

def main(request):
    return render(request, 'main.html')

def index(request):
    users = crud.objects.all()
    return render(request, 'index.html' , {'users':users})

def create(request):
    return render(request,'create.html')

def addusers(request):
    nameValue = request.POST.get("name")
    emailValue = request.POST.get("email")
    countryValue = request.POST.get("country")
    stateValue = request.POST.get("state")
    cityValue = request.POST.get("city")
    crud(uname=nameValue,email=emailValue,country=countryValue,state=stateValue,city=cityValue).save()
    send_mail("Your Data has been successfully stored","Hello {0},\n This is an test mail generated through code,\n Thank you... ".format(nameValue),"bunnygaganbunny@gmail.com",[emailValue],fail_silently=False)
    return redirect('index')

def edit(request,id):
    user = crud.objects.filter(id=id)[0]
    return render(request, 'edit.html', {"user":user})

def view(request,id):
    user = crud.objects.filter(id=id)[0]
    return render(request, 'view.html', {"user":user})

def updateuser(request,id):
    nameValue = request.POST.get("name")
    emailValue = request.POST.get("email")
    countryValue = request.POST.get("country")
    stateValue = request.POST.get("state")
    cityValue = request.POST.get("city")
    crud(id=id,uname=nameValue,email=emailValue,country=countryValue,state=stateValue,city=cityValue).save()
    return redirect('index')

def deleteuser(request,id):
    crud.objects.filter(id=id).delete()
    return redirect('index')

def generate(request):
    data = request.POST.get("data")
    img = make(data)
    img.save('static/img/test.png')
    return render(request,'main.html',{'data':data})