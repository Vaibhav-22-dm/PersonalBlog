from django.urls import path
from .views import *

urlpatterns = [
    path('getblogs/', getBlogs, name='get_blogs'),
    path('getblog/<int:pk>/', getBlog, name='get_blog'),
]