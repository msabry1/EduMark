from django.shortcuts import render
from home.loginandsignup import func
# Create your views here.
def contact(request):
    func(request)
    return render(request,"contact.html")