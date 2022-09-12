from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    newprice = models.FloatField(null=True,blank=True)
    rating = models.FloatField(null=True,blank=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    owner =  models.ForeignKey(User,on_delete=models.CASCADE)
    videos_number = models.IntegerField()
    videos_hours = models.FloatField()
    description = models.TextField()
    required_skills = models.TextField()
    course_image = models.ImageField(upload_to='courses/%Y/%m/%d')
    publish_date = models.DateTimeField(auto_now= True)


    def __str__(self):
        return self.name 


class Category(models.Model):
    name = models.CharField(max_length=50)
    publish_date = models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.name 