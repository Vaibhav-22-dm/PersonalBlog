import pytest
from django.contrib.auth.models import User
from tests.factories import *
from pytest_factoryboy import register
 
register(UserFactory)
register(BlogFactory)

# Arrange
@pytest.fixture()
def user(db):
    return User.objects.create(username='testuser',email='testuser@example.com')

@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username: str,
        password: str = None,
        first_name: str = "firstname",
        last_name: str = "lastname",
        email: str = "test@test.com",
        is_staff: str = False,
        is_superuser: str = False,
        is_active: str = True,
    ):

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )

        return user
    return create_app_user

@pytest.fixture
def new_user(db, new_user_factory): 
    return new_user_factory("Test_user", "password","MyName")
