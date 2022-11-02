from django.http import Http404
from django.shortcuts import render
from .models import *

def getBlogs(request):
    try:
        blogs = Blog.objects.all().order_by('date')
        context = {'blogs':blogs}
        return render(request, 'Blogs/index.html', context)
    except Exception as e:
        return render(request, 'Blogs/error.html')