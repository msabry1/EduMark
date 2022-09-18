from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    discount = models.FloatField(null=True,blank=True)
    rating = models.FloatField(null=True,blank=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    owner =  models.ForeignKey(User,on_delete=models.CASCADE)
    videos_number = models.IntegerField()
    videos_hours = models.IntegerField()
    tutorials = models.IntegerField()
    description = models.TextField()
    required_skills = models.TextField()
    course_image = models.ImageField(upload_to='courses_image/%Y/%m/%d',null=True)
    publish_date = models.DateTimeField(auto_now_add= True)



    def __str__(self):
        return self.name 


class Category(models.Model):
    name = models.CharField(max_length=50)
    publish_date = models.DateTimeField(auto_now_add= True)
    displayonsite = models.BooleanField(default=False,verbose_name='Display category on the site')
    def __str__(self):
        return self.name 