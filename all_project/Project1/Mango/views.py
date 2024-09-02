from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render
from Mango.models import Employee

# Create your views here.(functions)-
def view_home(request):
    # return render(request,'home.html')
   resp=render(request,'Mango/home.html')
   return resp

def contact_page(request):
    if request.method=="GET":
        page=render(request,"Mango/contact.html")
        return page
    elif request.method=="POST":
        n=request.POST.get("name","NA")
        a=int(request.POST.get("age",0))
        c=int(request.POST.get("num",0))
        f=request.POST.get("feed","NA")
        if 'send' in request.POST:
            d1={'n':n,'a':a,'c':c,'f':f}
            page=render(request,'Mango/contact.html',context=d1)
        return HttpResponse("</h2>Thankyou For Your Kind Feedback")
    else:
        pass

# Dataabase Connectivity in Django
def form(request):
    if request.method == "GET":
        # Render the form page
        return render(request, "Mango/form.html")
    elif request.method == "POST":
        # Create a new Employee instance
        emp = Employee()
        print (emp)
        # Set attributes using data from the POST request
        emp.name = request.POST.get("name", "NA")
        emp.age = int(request.POST.get("age", 0))
        emp.mobileNo = int(request.POST.get("num", 0))
        emp.city = request.POST.get("city", "NA")
        emp.salary = float(request.POST.get("sal", 0.0))
        emp.save()
        
        return HttpResponse("<h4>Form submitted successfully</h4>")



def view_dtl(request):
    if request.method=="GET":
        resp=render(request,'Mango/dtl.html')
        return resp
    elif request.method=="POST":
        a=int(request.POST.get("txt1",0))
        b=int(request.POST.get("txt2",0))
        
        if 'getresponse' in request.POST:
            if a>b:
                c=a
            else:
                c=b
        d1={'a':a,'b':b,'c':c}
        resp=render(request,'Mango/dtl.html',context=d1)
        return resp
    else:
        pass

class Employees:
    def __init__(self, name, age, city, salary):
        self.name = name
        self.age = age
        self.city = city
        self.salary = salary

def n_employee(n):
    ly = []
    names = ["Hritz Dubey", "Hridya", "Rebecka", "Kashvi"]
    ages = [22, 21, 19, 25]
    cities = ["Faridabad", "Bengaluru", "UK", "Turkey"]
    salaries = [15000, 14500, 29000, 40000]

    for i in range(n):
        emp1 = Employees(
            name=names[i % len(names)],
            age=ages[i % len(ages)],
            city=cities[i % len(cities)],
            salary=salaries[i % len(salaries)]
            # to fetch according to index no
            # name=names[i],
            # age=ages[i],
            # city=cities[i],
            # salary=salaries[i],
        )
        ly.append(emp1)
    return ly

# Example usage:
employees = n_employee(4)
for emp in employees:
    print(f"Name: {emp.name}, Age: {emp.age}, City: {emp.city}, Salary: {emp.salary}")

        
def view_dtlex(request):
    if request.method=="GET":
         return render(request,'Mango/dtl1.html')
    elif request.method=="POST":
         if "btn" in request.POST:
            t=int(request.POST.get("txtfield",0))
            print(t)
            emp_ly=n_employee(t)
            d2={"employee":emp_ly}
            res=render(request,'Mango/dtl1.html',context=d2)
            return res





