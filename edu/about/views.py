from django.shortcuts import render
from home.loginandsignup import func
# Create your views here.
def about(request):
    func(request)
    return render(request,"about.html")