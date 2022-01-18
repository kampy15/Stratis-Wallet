from django.shortcuts import render, HttpResponse,redirect
from wallet.forms import registerform
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
    return render(request,'index.html')
def login(request):
    if request.method == "POST":
            fname = request.POST['fname']
            pwd = request.POST['pwd']
            
            user = auth.authenticate(request, username=fname,password=pwd)
            
            if user is not None:
                auth.login(request, user)
                return redirect('main')
            else:
                return redirect("signup")
            
    return render(request,'login.html')
def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        uname = request.POST['uname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        
        user = User.objects.create( username = fname, email=email,password=pwd)
        user.save();
        return redirect('login')
    return render(request,'signup.html')
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


def logoutpage(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('/')