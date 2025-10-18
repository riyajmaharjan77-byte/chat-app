from django.shortcuts import render, redirect
from .models import Message, User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home_view(request):
    if request.method== 'POST':
        user_message= request.POST.get('user_message')
        Message.objects.create(message=user_message)
    users = User.objects.all()
    return render(request,'index.html', {'users':users})
def register_view(request):
    if request.method=="POST":
        error_message=""
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        hash_password=make_password(password)
        try:
            user_queryset=User.objects.get(username=username)
        except:
            user_queryset = None

        if user_queryset !=None:
            error_message +="username already exists"

        if username =='':
            error_message +="username required"
        if password=='':
            error_message +="password required"
        if email=='':
            error_message +="email required"

        if '@' in email:
            split_email=email.split('@')    
            if '.com' not in split_email[1]:
                error_message += 'email is not valid'

        else:
            error_message +='email not valid'
        if error_message =='':
            User.objects.create(username=username,email=email,password=hash_password)
        return render(request,'register.html',context={'error':error_message} if error_message!= '' else {'success':'registered successfully'})

    return render(request,'register.html')

def login_view(request):
    if request.method=='POST':
        error_message=''
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username=='':
            error_message+='username is required'
        if password=='':
            error_message+='password is required'

        user=authenticate(username=username,password=password)
        if user== None:
            error_message='invalid credential!'
        if error_message=='':
            login(request,user)
            return redirect('home')

        return render(request,'login.html', context={'error':error_message})

    return render(request,'login.html')