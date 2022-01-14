from django.test import TestCase
from ..models import *


class ParentTestCase(TestCase):
    """
    - Setting up Parent User
    - Inserting data
    """

    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Saif",
            last_name="Newaz",
            street="Bou Baazar",
            city="Dhaka",
            state="Dhaka",
            zip_code=1206
        )

    """
    - Testing if the data are returing correctly
    """

    def test_values_returned_correctly(self):
        self.assertEqual(self.parent.first_name, 'Saif')
        self.assertEqual(self.parent.last_name, 'Newaz')
        self.assertEqual(self.parent.street, 'Bou Baazar')
        self.assertEqual(self.parent.city, 'Dhaka')
        self.assertEqual(self.parent.state, 'Dhaka')
        self.assertEqual(self.parent.zip_code, 1206)


class ChildTestCase(TestCase):
    """
    - Setting up Parent User
    - Setting up Child User
    - Inserting data
    """

    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Saif",
            last_name="Newaz",
            street="Bou Baazar",
            city="Dhaka",
            state="Dhaka",
            zip_code=1206
        )

        self.child = Child.objects.create(
            parent=self.parent,
            first_name="Saisha",
            last_name="Newaz",
        )

    """
    - Testing if the data are returing correctly
    """

    def test_values_returned_correctly(self):
        self.assertEqual(self.child.first_name, 'Saisha')
        self.assertEqual(self.child.last_name, 'Newaz')
        self.assertEqual(self.child.parent.first_name, 'Saif')
