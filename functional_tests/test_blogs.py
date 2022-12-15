from selenium import webdriver
from Blogs.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.common.by import By

class TestBlogsListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
        self.user = User.objects.create(username="user_001", email="user_001@example.com")
        self.user.set_password('wordpass123')

    def tearDown(self):
        self.browser.close()

    def test_no_blogs_list_is_displayed(self):
        print("Reached")
        self.browser.get('http://127.0.0.01:8000/blogs/getblogs/')
        print("Done")
        # print(self.browser.get(self.live_server_url))
        time.sleep(5)
        # The user requests the page for the first time
        alert = self.browser.find_element(By.CLASS_NAME, "alert")
        print("This is element:",alert.text)
        self.assertEquals(
            alert.text,
            "Sorry, There are no blogs added yet."
        )

