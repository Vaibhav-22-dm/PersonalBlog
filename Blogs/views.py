from django.http import Http404
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import BlogCreationForm

def getBlogs(request):
    try:
        blogs = Blog.objects.all().order_by('-date')
        context = {'blogs':blogs}
        return render(request, 'Blogs/index.html', context)
    except Exception as e:
        context = {'error':str(e)}
        return render(request, 'Users/error.html', context)

def getBlog(request, pk):
    try:
        print(pk)
        blog = Blog.objects.get(id=pk)
        context = {'blog':blog}
        return render(request, 'Blogs/blog.html', context)
    except Exception as e:
        context = {'error':str(e)}
        return render(request, 'Users/error.html', context)


@login_required
def getMyBlogs(request):
    try:
        blogs = Blog.objects.filter(author=request.user)
        context = {'blogs':blogs}
        return render(request, 'Blogs/index.html', context)
    except Exception as e:
        context = {'error':str(e)}
        return render(request, 'Users/error.html', context)

@login_required
def addBlog(request):
    try:
        context={}
        if request.method == "POST":
            form = BlogCreationForm(request.POST)
            if form.is_valid():
                blog = form.save()
                blog.author = request.user
                blog.save()
                context["message"]="Blog added successfully"
                return redirect("../../blogs/getmyblogs/")
            else:
                print("Reached", form.errors)
                context["form_errors"]=form.errors
        form = BlogCreationForm()
        context["creation_form"] = form
        return render (request, "Blogs/create.html", context)
    except Exception as e:
        context = {'error':str(e)}
        return render(request, 'Users/error.html', context)
    
