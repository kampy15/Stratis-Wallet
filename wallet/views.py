from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse,redirect
from wallet.forms import registerform


# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
    return render(request,'index.html')
def main(request):
    return render(request,'main.html')
def newTxn(request):
    return render(request,'newTxn.html')
def oldTxn(request):
    return render(request,'oldTxn.html')
def profile(request):
    return render(request,'profile.html')
def wallet(request):
    return render(request,'wallet.html')




def register(request):
    form = registerform()
    if request.method=="POST":
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect("login")
    context = {'forms':form}
    return render(request,"signup.html",context)


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

