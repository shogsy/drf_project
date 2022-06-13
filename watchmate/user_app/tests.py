# from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
# from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username": "testcase",
            "email": "test@example.com",
            "password": "New Password22",
            "password2": "New Password22"
        }
        response = self.client.post(reverse('account:register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_OK)


