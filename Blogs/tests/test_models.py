from django.test import TestCase, Client
from Blogs.models import *

class TestModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="user_001", email="user_001@example.com")
        self.user.set_password("wordpass123")
        self.blog = Blog.objects.create(
            title="This is a title to a blog.",
            content="This is the content to the blog.",
            author=self.user
            )
        
    def test_blog_str_method(self):
        self.assertEquals(self.blog.__str__(), "This is a title to a blog.")