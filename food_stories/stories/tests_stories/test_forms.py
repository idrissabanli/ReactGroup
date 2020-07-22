from django.test import TestCase
from stories.forms import ContactForm


class ContactFormTestCase(TestCase):

    def setUp(self):
        self.valid_data = {
            'user_name': 'Tural Seferli',
            'user_email': 'tural@gmail.com',
            'subject': 'Saytda recipe elave ede bilmirem',
            'message': 'Recipe elave etmek ucun sehifeni mene gonderin...'
        }
        self.invalid_data = {
            'user_name': 'Tural Seferli',
            'user_email': 'tural@gmail.com',
        }
        self.invalid_data2 = {
            'user_name': 'Tural SeferliTural SeferliTural SeferliTural SeferliTural Seferli',
            'user_email': 'tural',
            'subject': 'Saytda recipe elave ede bilmirem2',
            'message': 'Recipe elave etmek ucun sehifeni mene gonderin2...'
        }

    def test_valid_data(self):
        form = ContactForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = ContactForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors.keys())
        self.assertIn('message', form.errors.keys())
        self.assertIn('This field is required.', form.errors['subject'])
        self.assertIn('This field is required.', form.errors['message'])

    def test_invalid_data2(self):
        form = ContactForm(data=self.invalid_data2)
        self.assertFalse(form.is_valid())
        self.assertIn('user_name', form.errors.keys())
        self.assertIn('user_email', form.errors.keys())
        self.assertIn('Ensure this value has at most 50 characters (it has 65).', form.errors['user_name'])
        self.assertIn('Enter a valid email address.', form.errors['user_email'])
