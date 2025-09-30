from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from . models import CustomUser

# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else :
            messages.error(request, "Username Or Password is Incorrect")
    return render(request, "login_page.html")

def sign_up_page(request):
    if request.method == "POST":
        uname = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        password = request.POST.get("password")
        con_password = request.POST.get("confirm_password")

        if password != con_password:
            messages.error(request, 'Password Do Not Match')
            return redirect(request, "sign_up.html")

        if User.objects.filter(username = uname).exists():
            messages.error(request, 'Username is Already Exist')
            return redirect(request, "sign_up.html")

        user = User.objects.create_user(username=uname, email=email, password=password )
        user .save()
        customer = CustomUser.objects.create(
            owner = user,
            phone_number = phone,
            address = address
        )
        return redirect('home')
    return render(request, "sign_up.html")

def logout_user(request):
    logout(request)
    return redirect('home')
