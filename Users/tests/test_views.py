from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import json
from django.contrib.auth import authenticate, login, logout

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'testuser@22'
        self.password = 'secret@123'
        self.email = 'testuser@example.com'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_user_GET(self):

        response = self.client.get(reverse('login'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'Users/login.html')

    def test_login_user_POST(self):
        credentials = {
            "username" : self.username,
            "password" : self.password
        }
        
        response = self.client.post(reverse('login'), credentials, follow=True)

        self.assertEquals(response.status_code,200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'Blogs/index.html')

    def test_register_user_GET(self):

        response = self.client.get(reverse('register'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'Users/register.html')

    def test_register_user_POST(self):
        credentials = {
            "username" : "newtestuser",
            "password1" : "wordpass123",
            "password2" : "wordpass123",
            "email"    : "newtestuser@example.com"
        }

        response = self.client.post(reverse('register'), credentials, follow=True)

        self.assertEquals(response.status_code,200)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'Blogs/index.html')

    def test_logout_user_GET(self):
        self.client.login(username = self.username, password= self.password)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEquals(response.status_code,200)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTemplateUsed(response, 'Blogs/index.html')
        

