from django.shortcuts import render
from .models import   *

# Create your views here.
def home(request):
    global courses ,part
    courses=Course_name.objects.all()
    part=Add_course_part.objects.all()
    d={'courses':courses,'part':part}
    print(d)
    print(part)
    return render(request,'home.html',d)



def viewcourse(request,url):
    global urls
    courses=Course_name.objects.all()
    part=Add_course_part.objects.all()
    urls=Course_name.objects.get(url=url)
    fil=Add_course_part.objects.filter(cat=urls)
    print(fil)
    d={'courses':courses,'part':part,'urls':urls ,'fil':fil}
    return render(request,'viewpost.html',d)

def readpart(request,url):
    part1=Add_course_part.objects.get(url=url)
    part=Add_course_part.objects.all()
    courses=Course_name.objects.all()
    d={'courses':courses,'part':part,'part1':part1,}
    return render(request,'readpost.html',d)

