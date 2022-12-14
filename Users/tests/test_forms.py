from django.test import TestCase
from Users.forms import *

class TestForms(TestCase):

    def test_registration_user_form_valid_data(self):
        form = UserRegistrationForm(data={
            'username':'user_001',
            'email': 'user_001@example.com',
            'password1': 'wordpass123',
            'password2': 'wordpass123'
        })

        self.assertTrue(form.is_valid())

    def test_registration_user_form_no_data(self):
        form = UserRegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

