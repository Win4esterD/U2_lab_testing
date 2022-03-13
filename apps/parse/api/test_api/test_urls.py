from rest_framework.test import APITestCase
from django.urls import reverse

class TestingAPI(APITestCase):
    def test_get(self):
        url = 'http://127.0.0.1:8000/api/auth/sign-out'
        print(url)
        response = self.client.get(url)
        AssertEqual

