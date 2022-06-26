import email
from django.shortcuts import redirect, render
from Writer.models import CustomUser
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('Home')
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            register = CustomUser.objects.create_user(first_name = first_name,last_name =last_name,email = email,password = password1,gender = gender)
            register.save()
            return redirect('Home')
        else:
            messages.error(request,'Şifre yanlış')
            return render(request,'oturumislemleri/register.html')


    else:
        return render(request,'oturumislemleri/register.html')
def login_user(request):
    if request.user.is_authenticated:
        return redirect('Home')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email = email,password = password)
        if user is not None:
            login(request,user)
            return redirect("Home")

        else:   
            messages.error(request,'Email veya Şifre yanlış')
            return render(request,'oturumislemleri/login.html')
    return render(request,'oturumislemleri/login.html')

def logout_user(request):
    logout(request)
    return redirect('Home')