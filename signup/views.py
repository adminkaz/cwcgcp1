from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreateForm
#from django.http import HttpResponse

# Create your views here.

def index(request):
#    context = {"name": "saito"}
    if request.method == "GET":
        context = {"form": UserCreateForm}
        return render(request, "signup/home.html", context)
    #print("in index:", request.POST)
    form = UserCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "signup/home.html")
    else:
        return render(request, "signup/home.html", {"form": form})


def login_view(request):
    #email = "user1@gmail.com"
    #password = "user1"
    if request.method == "GET":
        return render(request, "signup/login.html")
    #print("request.POST:", dict(request.POST))    

    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, email=email, password=password)
    login(request, user)
    return render(request, "signup/login.html")


def logout_view(request):
    logout(request)
    return render(request, "signup/login.html")


