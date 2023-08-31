# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import SignupForm


def sign_up_view(request):
    form_errors = ['']

    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:login')
        else:
            form_errors = form.get_fields_errors(request)
    
    if form_errors[0] != '':
        error = form_errors
    else:
        error = ''
        
    form = SignupForm()
    return render(
        request=request, 
        template_name='registration/sign_up.html',
        context={
            'form': form,
            'username': request.POST.get('username') or '',
            'password1': request.POST.get('password1') or '',
            'password2': request.POST.get('password2') or '', 
            'error': error,
        },
    )


def login_view(request):
    form = None
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("panel:dashboard")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    

    form = AuthenticationForm() if form is None else form
    return render(
        request=request,
        template_name="registration/login.html",
        context={
            'login_form': form,
        },
    )


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("accounts:login")
