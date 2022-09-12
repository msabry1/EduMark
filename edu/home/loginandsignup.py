from .models import Profile
from django.contrib.auth.models import User
# Create your views here.
from re import match
from django.contrib import messages
from django.contrib import auth
def func(request):
        # Sign up
    if request.POST and 'rebtn' in request.POST:
        username = request.POST['username'] if request.POST['username'] else None
        address = request.POST['address'] if request.POST['address'] else None
        email = request.POST['email'] if request.POST['email'] else None
        password = request.POST['password'] if request.POST['password'] else None
        confirmpassword = request.POST['confirmpassword'] if request.POST['confirmpassword'] else None
        if username and address and match(r'''^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$''',email) and password and confirmpassword:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if password == confirmpassword:
                        newuser = User.objects.create_user(username=username,email=email,password=password)
                        newuser.save()
                        Profile(user=newuser,Address=address).save()
                        messages.success(request,"Done Created")
                    else :
                        messages.error(request,"Passwords Don't Match ")
                else :
                    messages.error(request,"Email is Taken")
            else :
                messages.error(request,"User name is Taken ")

        else :
            messages.error(request,"check empty fields")



    # Sign in 
    elif request.POST and 'lobtn' in request.POST:
        username = request.POST['username'] if request.POST['username'] else None
        password = request.POST['password'] if request.POST['password'] else None
        if username and password :
            user = auth.authenticate(username=username,password=password)
            if user :
                auth.login(request,user)
                messages.success(request,"Done Login")
            else :
                messages.error(request,"Username Or Email are inCorrect ")
        else :
            messages.error(request,"Check empty Fields ")