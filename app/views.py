from django.shortcuts import render

# Create your views here.

def rpage(request):
    return render(request,'rpage.html')
def world(request):
    return render(request,'world.html')
