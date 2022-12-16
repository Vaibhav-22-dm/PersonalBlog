import factory
from faker import Faker
from django.contrib.auth.models import User
from Blogs.models import Blog
from django.contrib.auth.hashers import make_password

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    password = make_password('wordpass123')
    is_active = True
    is_staff = True

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    content = fake.text()
    title = fake.text()
    author =  factory.SubFactory(UserFactory)