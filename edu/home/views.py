from .models import Profile
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
# Create your views here.
from re import match
from django.contrib import messages
from django.contrib import auth
from .loginandsignup import func
from courses.models import Course , Category

def homepage(request):
    func(request)
    return render(request,"index.html",context = {
        'courses':Course.objects.all().order_by('-publish_date') ,
        'category':Category.objects.filter(displayonsite=True),
    })


def logout(request):
    if request.user.is_authenticated :
        auth.logout(request)
    return redirect('home')
    