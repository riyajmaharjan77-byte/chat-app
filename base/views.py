from django.shortcuts import render, redirect
from .models import Message, User, friendrequest
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
@login_required(login_url='login')
def home_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        Message.objects.create(message=user_message)
    users = User.objects.all()
    return render(request,'index.html', {'users':users})

@login_required(login_url='login')
def friend_request_send_view(request):
    user= request.user
    if request.method=="POST":
        user_id=request.POST.get('request_user')
        request_user=User.objects.get(id=user_id)
        friendrequest.objects.create(request_user=request_user ,requested_by_user=user ,status='Pending')
    friend_request_querryset= friendrequest.objects.filter(requested_by_user=user).values_list('request_user')
    user_querryset=User.objects.all().exclude(id__in=friend_request_querryset).exclude(id=request.user.id)
    return render(request,'friendrequestsend.html', context={'users':user_querryset})

@login_required(login_url='login')
def friend_request_list_view(request):
    user=request.user
    querryset=friendrequest.objects.filter(request_user=user)
    return render(request,'friendrequestlist.html', context={'friend_requests':querryset})

@login_required(login_url='login')
def friend_request_delete_view(request,pk):
    querryset=friendrequest.objects.get(id=pk)
    querryset.delete()
    return redirect('friend_request_list_view')

@login_required(login_url='login')
def message_view(request,user_id):
    user = request.user
    try:
        receiver = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return redirect('user_list')

    messages = Message.objects.filter(Q(sender=user, receiver=receiver) | Q(sender=receiver, receiver=user)).order_by('id')

    if request.method == 'POST':
        text = request.POST.get('user_message')
        if text:
            Message.objects.create(sender=user, receiver=receiver, message=text)
            return redirect('message_view', user_id=user_id)

    return render(request, 'messageview.html', {'user': user,'receiver': receiver,'messages': messages})

@login_required(login_url='login')
def user_list_view(request):
    
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'userlist.html', {'users': users})

@login_required(login_url='login')
def friend_request_status_update_view(request,pk):
    querryset=friendrequest.objects.get(id=pk)
    if request.method=='POST':
        status=request.POST.get('status')
        querryset.status=status
        querryset.save()
    return render(request,'friendrequeststatusupdate.html', context={'friend_request':querryset})

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