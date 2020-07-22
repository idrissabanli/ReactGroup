from django.test import TestCase, RequestFactory
from django.urls import reverse_lazy
from stories.forms import ContactForm
from stories.views import ContactView


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.url = '/contact/'
        self.reversed_url = reverse_lazy('contact')
        self.valid_data = {
            'user_name': 'Tural Seferli',
            'user_email': 'tural@gmail.com',
            'subject': 'Saytda recipe elave ede bilmirem',
            'message': 'Recipe elave etmek ucun sehifeni mene gonderin...'
        }
        self.invalid_data = {
            'user_name': 'Tural Seferli',
            'subject': 'Saytda recipe elave ede bilmirem',
            'message': 'Recipe elave etmek ucun sehifeni mene gonderin...'
        }
        
    
    def test_reverse_url(self):
        self.assertEqual(self.url, self.reversed_url)

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

        self.assertIn('form', response.context)

    def test_context(self):
        factory = RequestFactory()
        request = factory.get(self.url)
        response = ContactView.as_view()(request)
        self.assertIsInstance(response.context_data, dict)
        self.assertIsInstance(response.context_data['form'], ContactForm)

    def test_post_request(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_post_request(self):
        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.", html=True)

        # self.assertRedirects(response, '/')

        # self.assertRedirects(response, self.url, status_code=200)
