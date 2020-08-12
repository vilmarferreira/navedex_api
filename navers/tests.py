from django.test import TestCase,Client
from rest_framework import status
import json
from users.tests import random_char

client = Client()

class CreateNewNaverTest(TestCase):
    def setUp(self):
        self.user_payload = {
            'email' :random_char(7)+"@gmail.com",
            'password':'senha1234',
            'password_confirm':'senha1234'
        }
        response = client.post(
            '/api-register/',
            data=json.dumps(self.user_payload),
            content_type='application/json',
        )
        self.token = response.data['token']
        self.invalid_payload = {
            'name': random_char(10),
            'job_role': 1
        }
        self.valid_payload = {
            'name':random_char(10),
            'birthdate':'01/01/1995',
            'admission_date':'01/01/2020',
            'job_role':1
        }
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + self.token,
        }
    def test_create_valid_naver(self):

        response = client.post(
            '/api/v1/navers',
            data=json.dumps(self.valid_payload),
            content_type='application/json',
            **self.auth_headers

        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_invalid_naver(self):

        response = client.post(
            '/api/v1/navers',
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
            **self.auth_headers

        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_authorization_create_unauthorized(self):
        response = client.post(
            '/api/v1/navers',
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UpdateDeleteNaverTest(TestCase):
    def setUp(self):

        self.user_payload = {
            'email': random_char(7) + "@gmail.com",
            'password': 'senha1234',
            'password_confirm': 'senha1234'
        }
        ##Create user get token auth
        response = client.post(
            '/api-register/',
            data=json.dumps(self.user_payload),
            content_type='application/json',
        )
        self.token = response.data['token']
        self.valid_payload_create = {
            'name':random_char(10),
            'birthdate':'01/01/1995',
            'admission_date':'01/01/2020',
            'job_role': 2
        }
        self.valid_payload_update = {
            'name':random_char(10),
            'birthdate':'01/01/1995',
            'admission_date':'01/01/2020',
            'job_role': 3
        }

        self.invalid_payload_update = {
            'name': random_char(10),
            'admission_date': '01/01/2020',
            'job_role': 3
        }
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + self.token,
        }
        response = client.post(
            '/api/v1/navers',
            data=json.dumps(self.valid_payload_create),
            content_type='application/json',
            **self.auth_headers

        )
        self.naver_id=response.data['id']
    def test_valid_update_naver(self):
        response = client.put(
            '/api/v1/navers/{0}'.format(self.naver_id),
            data=json.dumps(self.valid_payload_update),
            content_type='application/json',
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_naver(self):
        response = client.put(
            '/api/v1/navers/{0}'.format(self.naver_id),
            data=json.dumps(self.invalid_payload_update),
            content_type='application/json',
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_delete_naver(self):
        response = client.delete(
            '/api/v1/navers/{0}'.format(self.naver_id),
            content_type='application/json',
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
