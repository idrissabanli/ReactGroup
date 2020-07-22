from django.test import TestCase
from django.template import Template, Context
from stories.models import About


class SplitTagTestCase(TestCase):

    def setUp(self):
        self.value = "salam necesen?"
        context = {
            'value': self.value
        }
        context = Context(context)

        html = """
            {% load filters %}
            {{value|split_tag:" "}}
        """

        self.template = Template(html).render(context)

    def test_tag(self):
        expected_results = self.value.split(" ")
        actual_result = self.template
        for expected_result in expected_results:
            self.assertIn(expected_result, actual_result)

class GetAboutInfoTagTestCase(TestCase):

    def setUp(self):
        context = Context({})
        About.objects.create(title='Stories', phone_number="1221", location='23232', email='about@gmail.com', description='sdfdsf', daily_visitors=12, facebook_page_url='http://fb.com', instagram_page_url='http://instagram_page_url.com', twitter_page_url='http://twitter_page_url.com')

        html = """
            {% load custom_tags %}
            {% get_about_info as about_info %}
            {{about_info.title}}
        """
        self.template = Template(html).render(context)

    def test_tag(self):
        expected_result = About.objects.last()
        actual_result = self.template
        self.assertIn(expected_result.title, actual_result)
        