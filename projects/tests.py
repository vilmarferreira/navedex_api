import json

from django.test import TestCase,Client
from rest_framework import status

from navers.models import Naver
from projects.models import Project
from users.models import User
from users.tests import random_char

client = Client()

class CreateProjectTest(TestCase):
    def setUp(self):
        user = User(email='email@email.com')
        user.set_password('password1234')
        user.save()
        data_navers = [
            {
                'name': random_char(10),
                'birthdate': '1995-01-01',
                'admission_date':  '2020-01-01',
                'job_role': 3,
                'user': user
            },
            {
                'name': random_char(10),
                'birthdate': '1995-01-01',
                'admission_date': '2020-01-01',
                'job_role': 1,
                'user': user
            },
            {
                'name': random_char(10),
                'birthdate': '1995-01-01',
                'admission_date': '2020-01-01',
                'job_role': 2,
                'user': user
            },
        ]
        navers = []
        for nav in data_navers:
            naver =Naver(**nav)
            naver.save()
            navers.append(naver)

        response = client.post(
            '/api-token-auth/',
            data=json.dumps({'email':'email@email.com','password':'password1234'}),
            content_type='application/json',
        )

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + response.data['token'],
        }
        self.payload_valid = {
            'name':random_char(10),
            'navers': [x.id for x in navers]
        }
        self.payload_valid_update = {
            'name': random_char(10),
            'navers': [x.id for x in navers]
        }
        self.payload_valid_update = {
            'name': random_char(10),
            'navers': [
                navers[0].id,navers[1].id,
            ]
        }
        self.payload_invalid_update = {
            'name': random_char(10),
            'navers': [
                100,200,300
            ]
        }
        self.project = Project.objects.create(name=random_char(10),user=user)
        self.project.navers.add(*navers)
        self.project.save()
    def test_create_projet(self):
        response = client.post(
            '/api/v1/projects',
            data=json.dumps(self.payload_valid),
            content_type='application/json',
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_projet(self):
        response = client.put(
            '/api/v1/projects/{0}'.format(self.project.id),
            data=json.dumps(self.payload_valid_update),
            content_type='application/json',
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_navers(self):
        response = client.put(
            '/api/v1/projects/{0}'.format(self.project.id),
            data=json.dumps(self.payload_invalid_update),
            content_type='application/json',
            **self.auth_headers
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthorized_update(self):
        response = client.put(
            '/api/v1/projects/{0}'.format(self.project.id),
            data=json.dumps(self.payload_valid_update),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
