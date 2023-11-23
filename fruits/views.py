from django.shortcuts import render

# Create your views here.

def grapes(request):
    return render(request,'grapes.html')


def apple(request):
    return render(request,'apple.html')

def banana(request):
    return render(request,'banana.html')

