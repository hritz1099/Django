from django.shortcuts import *
from django.http import HttpResponse
from Core.models import *
from Core.forms import *
from django.http import *
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
    

# def Student_courseDetail(request):
#     # cid=int(request.POST.get('cid',0))
#     allcourse=Course.objects.all()
#     c=Course.objects.get(id=1)
#     allstu=c.student.all()
#     d1={'courses':allcourse}
#     d1['cid']=c.id
#     d1['cname']=c.name
#     d1={'students':allstu}
#     if request.method=="GET":
#          print(allcourse)
#          d1={'courses':allcourse}
#          return render(request,"Core/course.html",context=d1)
#     elif request.method=="POST":
#         cid=int(request.POST.get('cid',0))
#         c=Course.objects.get(id=cid)
#         allstu=c.student.all()
#         d1={'students':allstu}
#         return render(request,"Core/course.html",context=d1)

# def Student_courseDetail(request):
#     allcourse = Course.objects.all()

#     if request.method == "GET":
#         # On GET, we display the form with all courses.
#         d1 = {'courses': allcourse}
#         return render(request, "Core/course.html", context=d1)
    
#     elif request.method == "POST":
#         # On POST, retrieve the selected course and the associated students.
#         cid = int(request.POST.get('cid', 0))
#         if cid:
#             c = Course.objects.get(id=cid)
#             allstu = c.student.all()
#             d1 = {
#                 'courses': allcourse,  # Keep the courses in the context
#                 'cid': c.id,  # Set the selected course ID
#                 'cname': c.name,  # Set the selected course name for display
#                 'students': allstu  # Set the students enrolled in this course
#             }
#         else:
#             # Handle the case where no valid course is selected.
#             d1 = {
#                 'courses': allcourse,
#                 'students': [],
#                 'cname': 'None'  # Set a default value if no course is selected
#             }
        
#         return render(request, "Core/course.html", context=d1)
def Student_courseDetail(request):
    cid=int(request.POST.get('cid',0))
    allcourse = Course.objects.all()  
    c = Course.objects.get(id=1) 
    allstu = c.student.all()
    d1 = {
        'courses': allcourse,  
        'cid': c.id,           
        'cname': c.name,       
        'students': allstu    
    }
    if request.method == "GET":
        print(allcourse)
        return render(request, "Core/course.html", context=d1)
    elif request.method == "POST":
        cid = int(request.POST.get('cid', 0))
        c = Course.objects.get(id=cid)
        allstu = c.student.all()
        d1['cid'] = c.id
        d1['cname'] = c.name
        d1['students'] = allstu

        return render(request, "Core/course.html", context=d1)


def view_studentform(request):
    if request.method=="GET":
        frm_unbound=StudentForm()
        d1={'forms':frm_unbound}
        return render(request,"Core/stuform.html",context=d1)
    elif request.method=="POST":
       frm_bound=StudentForm(request.POST,files=request.FILES)
       if frm_bound.is_valid():
           frm_bound.save()
           response_html = """
                <h2>Student details saved successfully</h2>
                <form action="/coredetails/stuform" method="get">
                    <button type="submit">Back to Homepage</button>
                </form>
            """
           return  HttpResponse(response_html) 
        #    return redirect('homepage') 
       
       else:
           frm_bound=StudentForm()
           d1={'forms':frm_bound}
           print("error")
           return render(request,"Core/stuform.html",context=d1)
       
   
           
