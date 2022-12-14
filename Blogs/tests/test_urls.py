from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Blogs.views import *

class TestUrls(SimpleTestCase):

    def test_get_blogs_urls_resolves(self):
        url = reverse('get_blogs')
        print(resolve(url))
        self.assertEquals(resolve(url).func,getBlogs)
    
    def test_get_blog_urls_resolves(self):
        url = reverse('get_blog',args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, getBlog)

    def test_get_my_blog_urls_resolves(self):
        url = reverse('get_my_blogs')
        print(resolve(url))
        self.assertEquals(resolve(url).func, getMyBlogs)
    
    def test_add_blog_urls_resolves(self):
        url = reverse('add_blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func, addBlog)