from django.test import TestCase, Client
from django.urls import reverse
from Blogs.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="user_001", password="wordpass123")
        self.client.login(username="user_001", password="wordpass123")

        Blog.objects.create(
            title="This is title to the old blog.",
            content="This is the content of the old blog"
        )

    def test_get_blogs_GET(self):

        response = self.client.get(reverse('get_blogs'))

        self.assertEquals(response.status_code,200)
        self.assertEquals(response.context['blogs'].count(),1)
        self.assertTemplateUsed(response, 'Blogs/index.html')

    def test_get_blog_GET(self):
        blog = Blog.objects.create(title="Some Random Title", content="Some content which I will add later")

        response = self.client.get(reverse('get_blog', args=[str(blog.id)]))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'Blogs/blog.html')

    def test_get_my_blog_GET(self):

        response = self.client.get(reverse('get_my_blogs'))
        
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'Blogs/index.html')

    def test_add_blog_POST(self):

        data = {
            "title": "This is a blog title.",
            "content": "This is the content of a blog."
        }
        
        response = self.client.post(reverse('add_blog'), data, follow=True)

        self.assertEquals(response.status_code,200)
        self.assertEquals(response.context['blogs'].count(),1)
        self.assertTemplateUsed(response, 'Blogs/index.html')




