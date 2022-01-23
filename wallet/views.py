from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse,redirect
from pystratis.nodes import StraxNode
from typing import List
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
    return render(request,'index.html')
def main(request):
    return render(request,'main.html')
def newTxn(request):
    return render(request,'newTxn.html')
def oldTxns(request):
    return render(request,'oldTxns.html')
def profile(request):
    return render(request,'profile.html')
def wallet(request):
    return render(request,'wallet.html')


def register(request):
    
    if request.method=="POST":
        username = request.POST.get('name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        pas= request.POST.get('pas')
        pas2 = request.POST.get('pas2')
        
        user=User.objects.create_user(username=username,email=email,password=pas,)
        user.save()

        print("user created")
        node = StraxNode()
        mnemonic: List[str] = node.wallet.create(name=username, password=pas, passphrase='')       
        return redirect("login")
    
    return render(request,"signup.html")


def loginpage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pwd = request.POST.get('pas')
            
        user = authenticate(request, username=name,password=pwd)
        if user is not None:
            login(request,user)
            return redirect("main")
        else:
            return redirect("login")
            
    return render(request,"login.html") 
    

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        
    return redirect('login')

