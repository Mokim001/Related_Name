from django.urls import path
from app.views import *

urlpatterns=[
    path('',home,name='home'),
    path('insert_school',insert_school,name='insert_school'),
    path('insert_student',insert_student,name='insert_student'),
    path('slist',slist,name='slist'),
    path('display<pk>',display,name='display'),
]