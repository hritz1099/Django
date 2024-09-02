from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_site(request):
    #return HttpResponse("<h1>Welcome to my home page!!!!</h1>")
    return render(request,'EMS/home.html')
def contact_page(request):
    n=request.POST.get("name","NA")
    a=int(request.POST.get("age",0))
    c=request.POST.get("city","NA")
    s=int(request.POST.get("pin",0))
    if request.method=="GET":
       return render(request,'EMS/contact.html')
    elif request.method=="POST":
        if 'btnsubmit' in request.POST:
            d1={'n':n,'a':a,'c':c,'s':s}
            return  render(request,'EMS/contact.html',context=d1)
        
class Employee():
    def __init__(self):
        self.name=" "
        self.age=0
        self.city=" "
        self.salary=0
def n_employee(n):
    ly=[]
    for i in range(n):
        emp=Employee()
        emp.name ="Hritz Dubey"
        emp.age=22
        emp.city="Faridabad"
        emp.salary=15000
        ly.append(emp)
    return ly
        
def view_dtl(request):
    if request.method=="GET":
         return render(request,'EMS/dtl.html')
    elif request.method=="POST":
         if "btn" in request.POST:
            t=int(request.POST.get("txtfield",0))
            print(t)
            emp_ly=n_employee(t)
            d2={"employee":emp_ly}
            res=render(request,'EMS/dtl.html',context=d2)
            return res





        
         
