from django.shortcuts import render, redirect
from authentication.models import *
from authentication.forms import *
# Create your views here.
def main(request):
    if request.method =='POST':
        form = login(request.POST)
        return render(request, 'remark.html', {'form':form})
    else:
        form = login()
    return render(request, 'dashboard.html', {'form':form})


def remark(request):
    
    return render(request, 'remark.html')
    
