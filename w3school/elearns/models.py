from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
from tinymce.models import HTMLField

# Create your models here.

from django.db import models

# Create your models here.


class Course_name(models.Model):
    course_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    cat=models.CharField(max_length=50000)
    desc=HTMLField()
    url=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now=False, auto_now_add=False)
    image=models.ImageField(upload_to="course_pic/")

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html("<img src='/media/{}' style='width:40px; height:40px; border-radius:50%'/>".format(self.image))


class  Add_course_part(models.Model):
    part_title=models.CharField(max_length=200)
    cat=models.ForeignKey(Course_name,on_delete=models.CASCADE)
    url=models.CharField(max_length=200)
    content=HTMLField()
    date=models.DateField(auto_now=False, auto_now_add=False)
    image=models.ImageField(upload_to="course_part_pic/")


    def __str__(self):
        return self.part_title


    def image_tag(self):
        return format_html("<img src='/media/{}' style='width:40px; height:40px; border-radius:50%'/>".format(self.image))