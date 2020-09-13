from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

# Login 
# def Login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username= username, password= password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, 'This account is not exist')
#             return redirect('login')
#     else:
#         return render(request, 'login.html')

# # Logout
# def Logout(request):
#     auth.logout(request)
#     return redirect('/')

# # Register 
# def Register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         gender = request.POST['gender']
#         dateOfBirth = request.POST['dateOfBirth']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         is_shipper = request.POST['is_shipper']

#         if password1 == password2:

#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "This username is used")
#                 return redirect('register')

#             elif User.objects.filter(email=email).exist():
#                 messages.info(request, "This email is used")
#                 return redirect('register')

#             else:
#                 user = User.objects.create_user(username=username, password=password1, 
#                 email=email, first_name=first_name, last_name=last_name,
#                 dateOfBirth= dateOfBirth, gender= gender, is_shipper= is_shipper)
#                 user.save()  
#                 print("User created")
#                 return redirect('login')
#         else:
#             messages.info(request, "You must enter the same password twice in order to confirm it.")
#             return redirect('register')
            
#         return redirect('/')
#     else:
#         return render(request, 'register.html')

def Index(request):
    return render(request, 'index.html')
    
# def Food(request):
#     return render(request, 'foodpage.html')
# def Cart(request):
#     pass
# def Search(request):
#     return render(request, 'search.html')
