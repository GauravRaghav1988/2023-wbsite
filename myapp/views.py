from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def home(request):
    return render(request, 'index.html')


def register(request):
     if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
             messages.success(request, 'Account Created Successfully !!') 
            #  messages.add_message(request,messages.SUCCESS, "Your Account has been created! ")
             fm.save()
            #  return HttpResponseRedirect('/')
     else: 
      fm = SignUpForm()
     return render(request,'registration.html', {'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/')
        else: 
         fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
      return HttpResponseRedirect('/')
    

@login_required
def logoutuser(request):
    logout(request)
    return redirect('/')# Redirect to home or any other page

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update the session with the user's new password
            messages.success(request, 'Password Changed successfully !!')
            return redirect('/login/')  # Redirect to home page or any other page after password change
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'changepassword.html', {'form': form})


@login_required
def account(request):
    return render(request, 'account.html')