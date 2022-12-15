from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class TestUsersPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
        self.user = User.objects.create(username="user_001", email="user_001@example.com")
        self.user.set_password('wordpass123')

    def tearDown(self):
        self.browser.close()

    def test_user_login(self):
        print("Reached")
        self.browser.get('http://127.0.0.01:8000/users/login/')
        print("Done")
        # print(self.browser.get(self.live_server_url))
        time.sleep(5)
        # The user requests the page for the first time
        username = self.browser.find_element(By.NAME, "username")
        password = self.browser.find_element(By.NAME, "password")
        submit = self.browser.find_element(By.ID, "submit-btn")

        username.send_keys('mmayank446')
        password.send_keys('mishra644')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)
        print(self.browser.current_url)
        self.assertEquals(self.browser.current_url, 'http://127.0.0.1:8000/blogs/getblogs/')
