import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_set_check_password(user):
    # Act
    user.set_password('wordpass123')

    # Assert
    assert user.check_password('wordpass123') is True

@pytest.mark.django_db
def test_username(user):

    # Assert
    assert user.username == 'testuser'

@pytest.mark.django_db
def test_user_email(user):

    # Assert
    assert user.email == 'testuser@example.com'

def test_user_first_name(new_user):
    print('First name: ' + new_user.first_name)

    # Assert
    assert new_user.first_name == 'MyName'

def test_new_user(user_factory):
    print('New user: ' + user_factory.username)
    assert True

def test_new_user1(user_factory):
    user = user_factory.build()
    print('New user: ' + user.username)
    assert True
    
@pytest.mark.django_db
def test_new_user2(user_factory):
    user = user_factory.create()
    count = User.objects.all().count()
    print('count: ', count)
    print('New user: ' + user.username)
    assert True

@pytest.mark.django_db
def test_new_blog(db, blog_factory):
    blog = blog_factory.create()
    print('New blog Title: ' + blog.title)
    print('New blog Content: ' + blog.content)
    print('New blog Author: ' + blog.author.username)
    print('New blog Date: ' + str(blog.date))

    assert True



