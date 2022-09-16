from django.shortcuts import render
from .models import Course,Category
from django.db.models import Q
from home.loginandsignup import func
from django.core.paginator import Paginator
# Create your views here.
def courses(request):
    func(request)
    all = Course.objects.all().order_by('-publish_date')
    if request.GET.get('searchbar'):
        all =  all.filter(Q(name__icontains=request.GET['searchbar']) | Q(description__icontains=request.GET['searchbar'])| Q(required_skills__icontains=request.GET['searchbar']))
    paginator = Paginator(all,6)
    pagenum = request.GET.get('page')
    context = {
        'courses':paginator.get_page(pagenum),
        'category': Category.objects.filter(displayonsite=True),
    }
    return render(request,"courses.html",context)


def course(request,coid):
    func(request)
    return render(request,"course_details.html",{
        'course':Course.objects.get(id=coid),
        
    })