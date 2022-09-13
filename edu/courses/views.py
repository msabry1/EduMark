from django.shortcuts import render
from .models import Course,Category
from django.db.models import Q
from home.loginandsignup import func
# Create your views here.
def courses(request):
    func(request)
    all = Course.objects.all().order_by('-publish_date')
    if "searchbar" in request.GET:
        if request.GET['searchbar']:
            all =  all.filter(Q(name__icontains=request.GET['searchbar']) | Q(description__icontains=request.GET['searchbar'])| Q(required_skills__icontains=request.GET['searchbar']))
    context = {
        'courses':all
    }
    return render(request,"courses.html",context)


def course(request,coid):
    func(request)
    return render(request,"course_details.html",{
        'course':Course.objects.get(id=coid)
    })