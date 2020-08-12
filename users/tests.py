import json
import random
import string

from django.test import TestCase, Client
from rest_framework import status

# Create your tests here.
from users.models import User

client = Client()
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
class CreateNewUserTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'email' :random_char(7)+"@gmail.com",
            'password':'senha1234',
            'password_confirm':'senha1234'

        }
        self.invalid_payload_password = {
            'email': random_char(7) + "@gmail.com",
            'password': 'senha1234',
            'password_confirm': 'senha123'
        }
        self.invalid_payload_email = {
            'email': random_char(7),
            'password': 'senha1234',
            'password_confirm': 'senha1234'
        }
    def test_create_valid_user(self):
        response = client.post(
            '/api-register/',
            data = json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_invalid_email(self):
        response = client.post(
            '/api-register/',
            data=json.dumps(self.invalid_payload_password),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error']['message'], "The two password fields didn't match.")

    def test_create_invalid_email(self):
        response = client.post(
            '/api-register/',
            data=json.dumps(self.invalid_payload_email),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], "Enter a valid email address.")

class LoginTest(TestCase):
    def setUp(self):
        payload_valid_create = {
            'email': 'email@email.com',
            'password':'password123',
            'password_confirm': 'password123'
        }
        client.post(
            '/api-register/',
            data=json.dumps(payload_valid_create),
            content_type='application/json',
        )
        self.payload_valid_login = {
            'email': 'email@email.com',
            'password': 'password123',
        }
        self.payload_invalid_login = {
            'email': 'email@email1.com',
            'password': 'password123',
        }

    def test_login_valid(self):
        response = client.post(
            '/api-token-auth/',
            data = json.dumps(self.payload_valid_login),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_login_invalid(self):
        response = client.post(
            '/api-token-auth/',
            data = json.dumps(self.payload_invalid_login),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)





