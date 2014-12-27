import datetime

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from facts.models import Fact
from facts.views import home_page


class HomePageTest(TestCase):

    def test_facts_url_resolves_to_facts_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('facts/home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_uses_home_template(self):
        request = HttpRequest()
        response = home_page(request)

        self.assertTemplateUsed(response, 'facts/home.html')

    def test_home_page_contains_list_of_facts(self):
        Fact.objects.create(text="Fact 1")
        Fact.objects.create(text="Fact 2")

        request = HttpRequest()
        response = home_page(request)

        self.assertContains(response, "Fact 1")
        self.assertContains(response, "Fact 2")


class FactModelTest(TestCase):
    def test_saving_and_retrieving_facts(self):
        first_fact = Fact.objects.create(text="This is the first fact")
        second_fact = Fact.objects.create(text="This is the second fact")

        saved_facts = Fact.objects.all()
        self.assertEqual(saved_facts.count(), 2)

        self.assertEqual(saved_facts[0].text, "This is the first fact")
        self.assertEqual(saved_facts[1].text, "This is the second fact")

    def test_facts_are_in_reverse_date_order(self):
        first_fact = Fact.objects.create(text="Later fact")
        second_fact = Fact.objects.create(
            text="Earlier fact",
            timestamp=datetime.datetime.now() - datetime.timedelta(days=3)
            )
        saved_facts = Fact.objects.all()

        self.assertEqual(saved_facts[0].text, "Later fact")
        self.assertEqual(saved_facts[1].text, "Earlier fact")

    def test_unicode(self):
        fact = Fact.objects.create(text="This is the first fact")

        self.assertEqual(fact.__unicode__(), "This is the first fact")


# from cms_app import FactApphook
#
# class ApphookTest(TestCase):
#     self.assertEqual(FactApphook.name, "Facts")
#     self.assertEqual(FactApphook.urls, "facts.urls")
#
