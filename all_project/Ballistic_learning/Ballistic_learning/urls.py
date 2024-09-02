"""
URL configuration for Ballistic_learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render


def view_calc(request):
     a=int(request.POST.get('txt1',0))
     b=int(request.POST.get('txt2',0))
     if request.method=="GET":
          resp=render(request,'calc.html')
          return resp
     elif request.method=="POST":
          if 'btnsum' in request.POST:
               res=a+b
              
          elif 'btnsub' in request.POST:
               res=a-b
               
          elif 'btnmulti' in request.POST:
               res=a*b
               
          elif 'btndiv' in request.POST:
               res=a/b
          d1={'a':a,'b':b,'res':res}
          resp=render(request,'calc.html',context=d1)
          return resp    
         
        
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calc/', view_calc),
    path('emsapp/',include('EMS.urls'))
    

]
