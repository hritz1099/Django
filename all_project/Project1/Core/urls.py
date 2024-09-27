from django.urls import path
from .views import *


#baseUrl:-http://127.0.0.1:8000/coredetails

urlpatterns = [
    path('details/',core_details,name="details"),
    path('pay/',get_paymentData,name="get_paymentData"),
    path('course/',Student_courseDetail,name="Student_courseDetail"),
    path('stuform/',view_studentform,name="Student_Form"),
    # path('',view_studentform,name="homepage"),
]



