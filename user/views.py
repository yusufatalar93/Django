from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username =username)
            newUser.set_password(password)
            newUser.save()
            messages.info(request,"Başarıyla kayıt oldunuz...")
            login(request,newUser)
            return redirect("index")
        context = {
            "form": form
        }
        return render(request,"register.html",context)   

    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request,"register.html",context)


def loginuser(request):
    form = LoginForm(request.POST or None)
    context = {
            "form": form
        }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        User = authenticate(username = username,password = password)
        if User is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"login.html",context)
        else:
             messages.success(request,"Başarılı bir giriş yaptınız")
             login(request,User)
             return redirect("index")
    context = {
            "form": form
        }

    return render(request,"login.html",context)
def logoutuser(request):
    logout(request)
    messages.warning(request,"Başarıyla çıkış yaptınız")
    return redirect("index")
