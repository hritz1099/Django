from django.shortcuts import *
from django.http import HttpResponse
from Core.models import *
# Create your views here.


def core_details(request):
    return HttpResponse("Welcome to Core Details")

def get_paymentData(request):
    if request.method=="GET":
        return render(request,"Core/pay.html")
    elif request.method=="POST":
        txtid=int(request.POST.get('Sid',0))
        stu=Student.objects.get(id=txtid)
        allpay=stu.paymentdetails_set.all()
        print(allpay,stu)
        d1={'payments':allpay,"stu":stu}
        return render(request,"Core/pay.html",context=d1)
    

def Student_courseDetail(request):
    if request.method=="GET":
         allcourse=Course.objects.all()
         print(allcourse)
         d1={'courses':allcourse}
         return render(request,"Core/course.html",context=d1)
    elif request.method=="POST":
        cid=int(request.POST.get('cid',0))
        c=Course.objects.get(id=cid)
        allstu=c.student.all()
        d1={'students':allstu}
        
        return render(request,"Core/course.html",context=d1)

