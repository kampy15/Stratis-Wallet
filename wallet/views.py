from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
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
