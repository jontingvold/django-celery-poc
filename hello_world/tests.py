from django.test import TestCase
from .models import Person

class PersonTestCase(TestCase):
    def test_create_person(self):
        """Animals that can speak are correctly identified"""
        name = "Per"
        person = Person(name=name)
        self.assertEqual(person.name, name)
