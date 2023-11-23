from animals.views import *
from django.urls import path

app_name='animals'

urlpatterns=[
    path('cow/',cow,name='cow'),
    path('dog/',dog,name='dog'),
    path('cat/',cat,name='cat'),
]