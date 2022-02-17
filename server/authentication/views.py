from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'dashboard.html')
    
def remark(request):
    return render(request, 'remark.html')