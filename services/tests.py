from django.test import TestCase
import unittest
from django.test import Client


# Unit test to check services view
class ServicesViewTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/services/')
        self.assertEqual(response.status_code, 200)


# Unit test to check service_detail view
class ServiceDetailViewTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/services/1/')
        self.assertEqual(response.status_code, 200)
