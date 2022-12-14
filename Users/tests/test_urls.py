from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Users.views import *

class TestUrls(SimpleTestCase):

    def test_login_urls_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func,userLogin)
    
    def test_register_urls_resolves(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, userRegister)

    def test_logout_urls_resolves(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, userLogout)