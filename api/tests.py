from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from .services import get_age_and_dob, get_age_from_agify

class AgifyAPITests(TestCase):

    @patch('requests.get')
    def test_get_age_from_agify(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'count': 298219, 'name': 'michael', 'age': 63}
        age = get_age_from_agify('michael')
        self.assertEqual(age, 63)

class HumanAgeAPITests(APITestCase):

    def test_human_age_api(self):
        url = reverse('human-age-api')
        data = {'name': 'michael'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'michael')
        self.assertTrue('age' in response.data)
        self.assertTrue('date_of_birth' in response.data)
