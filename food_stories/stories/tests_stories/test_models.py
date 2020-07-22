from django.test import TestCase
from stories.models import Contact


class ContactTestCase(TestCase):

    def setUp(self):
        self.data = {
            'user_name': 'Tural Seferli',
            'user_email': 'tural@gmail.com',
            'subject': 'Saytda recipe elave ede bilmirem',
            'message': 'Recipe elave etmek ucun sehifeni mene gonderin...'
        }
        self.data2 = {
            'user_name': 'Tural Seferli',
            'user_email': 'tural@gmail.com',
            'subject': 'Saytda recipe elave ede bilmirem2',
            'message': 'Recipe elave etmek ucun sehifeni mene gonderin2...'
        }
    
    # def test_creating(self):
        self.content = Contact.objects.create(**self.data)
        self.content2 = Contact.objects.create(**self.data2)

    def test_created_data(self):
        contact1 = Contact.objects.get(id=1)
        contact2 = Contact.objects.get(id=2)
        self.assertEqual(contact1, self.content)
        self.assertEqual(contact2, self.content2)


    def test_str_method(self):
        expected_result = self.content.user_name
        actual_result = self.content.__str__()

        self.assertEqual(expected_result, actual_result)

        expected_result = self.content2.user_name
        actual_result = self.content2.__str__()

        self.assertEqual(expected_result, actual_result)


