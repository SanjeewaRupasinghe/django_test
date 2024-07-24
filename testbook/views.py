from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print('index')
    # return HttpResponse("Hello test app")
    return render(request,'base.html')
