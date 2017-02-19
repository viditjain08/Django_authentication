from django.shortcuts import render
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from main.forms import loginform, signupform
from django.contrib.auth.decorators import login_required
from main.models import Erpuser
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            form = loginform(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                username1 = cd['username']
                password1 = cd['password']
                user = authenticate(username=username1, password=password1)
                if user is not None:
                    authlogin(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    form.add_error('username', 'Incorrect login credentials')
                    return render(request, 'login.html', {'form': form})
        else:
            #return HttpResponse('D')
            form = loginform()
            return render(request, 'login.html', {'form': form})
        return render(request, 'login.html', {'form': form})
@login_required(login_url='/login/')
def home(request):
    return render(request, 'main.html')

def logout(request):
    authlogout(request)
    return HttpResponseRedirect('/login/')

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            form = signupform(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                username2 = cd['username']
                firstname2 = cd['firstname']
                lastname2 = cd['lastname']
                email2 = cd['email']
                bitsid2 = cd['bitsid']
                password2 = cd['password2']
                us = Erpuser(first_name = firstname2, last_name = lastname2, username = username2, email=email2, bitsid = bitsid2)
                us.set_password(password2)
                us.save()
                return HttpResponseRedirect('/login/')
            else:
                return render(request, 'signup.html', {'form': form})
        else:
            form = signupform()
            return render(request, 'signup.html', {'form': form})
