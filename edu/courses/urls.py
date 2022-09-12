from django.urls import path
from . import views 
urlpatterns =  [
        path("",views.courses,name="courses"),
        path('<int:coid>/',views.course,name="course") ,


    
]