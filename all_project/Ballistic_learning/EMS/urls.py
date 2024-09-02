from django.urls import path 
from .views import *
#base url->>http://127.0.0.1:8000/emsapp/

urlpatterns=[
path('home/',home_site),
path('contact/',contact_page),
path('dtlex/',view_dtl),


]