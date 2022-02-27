from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from authentication.forms import *
from authentication.models import *
# Create your views here.

def homeView(request):
  return redirect('login')

def loginView(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():      
      user = authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password'])
      if user is None:
        messages.error(request,"Such user doesn't exist")
      else:
        login(request,user)
        return HttpResponse("You are succesfully logged in")
        
    else:
      for error_field in form.errors:
        for error in form.errors[error_field]:
          messages.error(request,error)
  else:
    form = LoginForm()

  return render(request,'login.html',{
    'form' : form
  })

def registerView(request):
  if request.method == 'POST':
    form = Create_User_Form(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
      user = User(first_name = form.cleaned_data['first_name'],
                  last_name=form.cleaned_data['last_name'],
                  email = form.cleaned_data['email'],
                  phone_number = form.cleaned_data['phone_number'],
                )
      user.set_password(form.cleaned_data['password1'])
      user.save()
      messages.success(request,"You have sucessfully registered!")
      return redirect('login')
    else:
      for error_field in form.errors:
        for error in form.errors[error_field]:
          messages.error(request,error)
  else:
    form = Create_User_Form()

  return render(request,'register.html',{
    'form' : form
  })

def logoutView(request):
  logout(request)
  return redirect('home')
  