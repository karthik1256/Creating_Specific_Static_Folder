from django.shortcuts import render

# Create your views here.
def dog(request):
    return render(request,'dog.html')

def cow(request):
    return render(request,'cow.html')

def cat(request):
    return render(request,'cat.html')
