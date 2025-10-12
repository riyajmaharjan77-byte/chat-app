from django.shortcuts import render
from .models import Message, User
# Create your views here.
def home(request):
    if request.method== 'POST':
        user_message= request.POST.get('user_message')
        Message.objects.create(message=user_message)
    users = User.objects.all()
    return render(request,'index.html', {'users':users})