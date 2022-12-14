from django.test import TestCase
from Blogs.forms import *
from django.contrib.auth.models import User

class TestForms(TestCase):

    def test_creation_blog_form_valid_data(self):
        user = User.objects.create(username="user_001", email="user_001@example.com")
        user.set_password("wordpass123")
        form = BlogCreationForm(data={
            'title':'This is a title to a blog.',
            'content': 'This is the content to a blog.'
        })

        self.assertTrue(form.is_valid())

    def test_creation_blog_form_no_data(self):
        form = BlogCreationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

