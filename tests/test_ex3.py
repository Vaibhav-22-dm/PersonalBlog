import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_create():
    user = User.objects.create(username='testuser',email='testuser@example.com')
    user.set_password("wordpass123")
    count = User.objects.all().count()
    print("count: ", count)
    assert 1 == count