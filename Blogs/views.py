from django.http import Http404
from django.shortcuts import render
from .models import *

def getBlogs(request):
    try:
        blogs = Blog.objects.all().order_by('date')
        context = {'blogs':blogs}
        return render(request, 'Blogs/index.html', context)
    except Exception as e:
        context = {'error':str(e)}
        return render(request, 'Blogs/error.html', context)

def getBlog(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
        context = {'blog':blog}
        return render(request, 'Blogs/blog.html', context)
    except Exception as e:
        context = {'error':str(e)}
        return render(request, 'Blogs/error.html', context)