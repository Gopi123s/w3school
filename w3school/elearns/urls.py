from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('blog/<slug:url>', viewcourse),
    path('post/<slug:url>', readpart),
     path('tinymce/', include('tinymce.urls')),
  
  ]
