from django.contrib import admin
from .models import *

# Register your models here.

class Course_nameAdmin(admin.ModelAdmin):
    list_display=('title','url','date','image_tag')
    search_fields=('title',)
    list_filter=('title','date')
    
class Addcourseadmin(admin.ModelAdmin):
    list_display=('part_title','cat','url','date','image_tag')
    search_fields=('cat',)
    list_filter=('cat','date')
    



admin.site.register(Course_name,Course_nameAdmin)
admin.site.register(Add_course_part,Addcourseadmin)


