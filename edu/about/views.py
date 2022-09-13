from django.shortcuts import render
from home.loginandsignup import func
from courses.models import Course
# Create your views here.

def calc(cls):
    totalhours = 0
    totalvideonumber = 0
    totalTutorialsnumber = 0
    for num in cls.objects.all():
        totalhours += num.videos_hours
        totalvideonumber += num.videos_number
        totalTutorialsnumber += num.tutorials
    return totalhours,totalvideonumber ,totalTutorialsnumber




def about(request):
    func(request)
    x,y,z = calc(Course)
    return render(request,"about.html",{
        "cousecount":Course.objects.count(),
        "totalhours" : x ,
        "totalvideonumber" : y ,
        "totalTutorialsnumber" : z

    }
    
    
    )