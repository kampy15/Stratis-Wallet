from importlib.resources import contents
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse,redirect
from matplotlib.style import context
from pystratis.nodes import StraxNode
from typing import List
from django.contrib.auth.models import User
from pystratis.core.networks import StraxTest


def index(request):
    return render(request,'index.html')
def main(request):
    return render(request,'main.html')
def newTxn(request):
    return render(request,'newTxn.html')
def oldTxns(request):
    return render(request,'oldTxns.html')
def profile(request):
    current_user = str(request.user)
    node = StraxNode(blockchainnetwork=StraxTest())
    unused_address = node.wallet.unused_address(wallet_name=current_user)
    wallet_balance = node.wallet.balance(
        wallet_name=current_user,
        include_balance_by_address=False
    )
    balance=wallet_balance.balances[0].amount_confirmed
    return render(request,'profile.html',{'add':unused_address,'bal':balance})
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
        node = StraxNode(blockchainnetwork=StraxTest())
        mnemonic: List[str] = node.wallet.create(name=username, password=pas, passphrase='') 
             
        # print(unused_address)
    
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

