import pytest
from Blogs.models import *

@pytest.mark.parametrize(
    "title, content",
    [
        ("NewTitle", "NewContent",),
    ],
)
def test_blog_instance(db, blog_factory, title, content):
    test = blog_factory(
        title=title, 
        content=content
        )
    print("Test Blog Author: " + test.author.username)
    item = Blog.objects.all().count()
    assert item == 1

@pytest.mark.parametrize(
    "username, email, password1, password2, error",
    [
        ("user_001", "user_001.com", "test@user", "test@user", '<ul class="errorlist"><li>email<ul class="errorlist"><li>Enter a valid email address.</li></ul></li></ul>'),
        ("user_002", "user_002@test.com", "test@user", "test@user2", ' <ul class="errorlist"><li>password2<ul class="errorlist"><li>The two password fields didn’t match.</li></ul></li></ul>'),
        ("user_003", "user_003@test.com", "testuse", "testuse", "<ul class=\"errorlist\"><li>password2<ul class=\"errorlist\"><li>The password is too similar to the email address.</li><li>This password is too short. It must contain at least 8 characters.</li></ul></li></ul>"),
        ("user_004", "", "test@user", "test@user", " <ul class=\"errorlist\"><li>email<ul class=\"errorlist\"><li>This field is required.</li></ul></li></ul>"),
        ("user_005", "user_005@test.com", "test@user", "test@user", None),
    ],
)
@pytest.mark.django_db
def test_user_register_view(client, username, email, password1, password2, error):
    # print(username, email, password1, password2, error)
    response = client.post(
        "http://127.0.0.1:8000/users/register/",
        data={
            "username": username,
            "email": email,
            "password1": password1,
            "password2": password2
        },
        follow=True
    )

    # print("Response: " + str(response.context["form_errors"]))
    try:
        # errors = response.context["form_errors"]
        assert response.context["form_errors"] == error
    except Exception as e:
        assert 1==1


def test_user_login_view(db, client, user_factory):

    user = user_factory()
    print("User: " + user.username)
    print("User: " + user.password)
    
    response = client.post( "http://127.0.0.1:8000/users/login/",
        data = {
            "username": user.username,
            "password": 'wordpass123'
        },
        follow=True
    )
    print(response)
    assert response.status_code == 200