from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

# Login 
def Login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'This account is not exist')
            return redirect('Login')
    else:
        return render(request, 'login.html')

# Logout
def Logout(request):
    auth.logout(request)
    return redirect('/')

# Register 
def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This username is used")
                return redirect('Register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email is used")
                return redirect('Register')

            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()  
                print("User created")
                return redirect('Login')
        else:
            messages.info(request, "You must enter the same password twice in order to confirm it.")
            return redirect('Register')
    else:
         return render(request, 'register.html')






def Index(request):
    return render(request, 'index.html')

def Food(request):
    return render(request, 'foodpage.html')

def Cart(request):
    pass

def Search(request):
    return render(request, 'search.html')
