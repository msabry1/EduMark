from .models import Profile
import requests 
from django.contrib.auth.models import User
# Create your views here.
from re import match
from django.contrib import messages
from django.contrib import auth
from django.conf import settings
def func(request):
        # Sign up
    if request.POST and 'rebtn' in request.POST:
        username = request.POST.get('username') if request.POST.get('username') else None
        address = request.POST.get('address') if request.POST.get('address') else None
        email = request.POST.get('email') if request.POST.get('email') else None
        password = request.POST.get('password') if request.POST.get('password') else None
        confirmpassword = request.POST.get('confirmpassword') if request.POST.get('confirmpassword') else None
        recaptcha = request.POST.get('g-recaptcha-response') if request.POST.get('g-recaptcha-response') else None
        if username and address and match(r'''^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$''',email) and password and confirmpassword:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if password == confirmpassword:
                        res = requests.post('https://www.google.com/recaptcha/api/siteverify',data={"secret":settings.RECAPTCHA_PRIVATE_KEY ,"response": recaptcha}).json()
                        print(res)
                        if res['success']:
                            newuser = User.objects.create_user(username=username,email=email,password=password)
                            newuser.save()
                            Profile(user=newuser,Address=address).save()
                            messages.success(request,"Done Created")
                        else :
                            messages.error(request,'Recaptcha Error ')
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
        username = request.POST.get('username') if request.POST.get('username') else None
        password = request.POST.get('password') if request.POST.get('password') else None
        if username and password :
            user = auth.authenticate(username=username,password=password)
            if user :
                auth.login(request,user)
                messages.success(request,"Done Login")
            else :
                messages.error(request,"Username Or Email are inCorrect ")
        else :
            messages.error(request,"Check empty Fields ")