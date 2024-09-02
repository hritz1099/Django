from django.urls import path
from .views import *
#http://127.0.0.1:8000/mangoapp
urlpatterns=[
    path('home/',view_home),
    path('contactUs/',contact_page), 
    path('dtlex/',view_dtl), 
    path('dtlexample/',view_dtlex), 
    path('form/',form),  
]
