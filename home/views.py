from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *



 
def home(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return render(request,'login.html')
def login_page(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        if request.method=="POST":
            username=request.POST['username']
            print(username)
            password=request.POST['password']
            print(password)
            print(username,password)
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('/home')
            else:
                return redirect('/login')
        else:
            return render(request,"login.html")

def signout(request):
    logout(request)
    return redirect('/login')      

   
def insertproject(request):
    pname=request.POST['projectName'];
    pdomain=request.POST['projectDomain'];
    pguide=request.POST['projectguide'];
    us=projectinfo(pname=pname, pdomain=pdomain,pguide=pguide);
    print(us)
    us.save();
    return render(request,'index.html')

def insertuser(request):
    lname=request.POST['leaderName'];
    lroll=request.POST['leaderRollNo'];
    m1n=request.POST['member1Name'];
    m1roll=request.POST['member1RollNo'];
    m2n=request.POST['member2Name'];
    m2roll=request.POST['member2RollNo'];
    m3n=request.POST['member3Name'];
    m3roll=request.POST['member3RollNo'];
    us=Groupinfo(ledname=lname, ledroll=lroll,mem1=m1n,mem1roll=m1roll,mem2=m2n,mem2roll=m2roll,mem3=m3n,mem3roll=m3roll);
    us.save();
    return render(request,'index.html')
    


# Create your views here.
