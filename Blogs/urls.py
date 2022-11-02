from django.urls import path
from .views import *

urlpatterns = [
    path('getblogs/', getBlogs, name='get_blogs'),
]