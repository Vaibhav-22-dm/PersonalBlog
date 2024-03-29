from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib import messages
# Create your views here.

def userLogin(request):
    try:
        context = {}
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None and user.is_authenticated:
                login(request, user)
                return redirect('../../blogs/getblogs')
            else:
                context["message"]="Credentials Invalid"
                print(context)
                return render(request, 'Users/login.html', context)
        return render(request, 'Users/login.html', context)
    except Exception as e:
        context={"error":str(e)}
        return render(request, 'Users/error.html', context)

def userRegister(request):
    context={}
    try:
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                context["message"]="Registration successful"
                return redirect("../../blogs/getblogs/")
            else:
                print(form.errors)
                context["form_errors"]=form.errors
        form = UserRegistrationForm()
        context["register_form"] = form
        return render (request, "Users/register.html", context)
    except Exception as e:
        return HttpResponse(str(e))

def userLogout(request):
    try:
        logout(request)
        return redirect('../../blogs/getblogs')
    except Exception as e:
        context = {"message":str(e)}
        return render(request, 'Users/error.html',context)