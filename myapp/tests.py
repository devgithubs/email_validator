from django.test import TestCase, Client
from django.urls import reverse
from .forms import TextForm

class TextFormTest(TestCase):
    def setUp(self):
        self.valid_data = {'text': 'example@example.com'}
        

    def test_disallowed_form_submission(self):
        c = Client()
        url = reverse('text_form')
        rep = c.post(url, self.valid_data)
        self.assertEqual(rep.status_code, 302)
        self.assertRedirects(rep, '/myapp/list/')

        
