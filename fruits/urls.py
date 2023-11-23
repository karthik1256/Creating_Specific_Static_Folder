from fruits.views import *
from django.urls import path

app_name='fruits'

urlpatterns=[
    path('apple/',apple,name='apple'),
    path('grapes/',grapes,name='grapes'),
    path('banana/',banana,name='banana'),
]
