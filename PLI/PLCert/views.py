from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'PLCert/index.html')



def about(request):
    return render(request, 'PLCert/about.html')

def courses(request):
    return render(request, 'PLCert/courses.html')