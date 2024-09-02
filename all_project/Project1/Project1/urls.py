"""
URL configuration for Project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

def view_welcome(request):
    return HttpResponse("<h1>Welcome To Django Views</h1>")

def view_sum(request,a,b):
    resp=HttpResponse("<h1>Welcome To Django Sum="+str(a+b)+"</h1>")
    return resp

def calc(request):
    if request.method == "GET":
         resp=render(request,'calc.html')
         return resp
    elif request.method == "POST":
         a=int(request.POST.get("txt1",0))
         b=int(request.POST.get("txt2",0))
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
    path('view/', view_welcome),
    path('sum/<int:a>/<int:b>', view_sum),
    path('calc/', calc),
    path('mangoapp/',include('Mango.urls'))#http://127.0.0.1:8000/mangoapp
]
