from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')
