from django.urls import path
from .views import *

urlpatterns = [
    path('login/', userLogin, name='login'),
    path('register/', userRegister, name='register'),
    path('logout/', userLogout, name='logout'),
]