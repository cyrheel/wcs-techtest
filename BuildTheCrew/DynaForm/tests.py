from django.test import TestCase
from django.test import Client


from .models import Argonaute

client = Client()


class Test_Name_Input(TestCase):

    def test_name_is_empty(self):
        response = client.post('/index/', {'your_name': '  '})
        self.assertEqual(response.status_code, 302)

    def test_name_is_not_alphabetic(self):
        response = client.post('/index/', {'your_name': ';:?!;;'})
        self.assertEqual(response.status_code, 302)
