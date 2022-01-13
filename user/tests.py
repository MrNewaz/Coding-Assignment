from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from .models import *


class ParentAPITests(APITestCase):

    # Setting up parent user
    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Saif",
            last_name="Newaz",
            street="Bou Bari Goli",
            city="Dhaka",
            state="Dhaka",
            zip_code=1206
        )

    # Get List of Parent Users
    def test_get_parent(self):
        client = APIClient()
        response = client.get("/user/parent/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Create Parent Users
    def test_parent_user_create(self):
        data = {
            "first_name": "Saif",
            "last_name": "Newaz",
            "street": "Bou Bari Goli",
            "city": "Dhaka",
            "state": "Dhaka",
            "zip_code": 1206
        }

        client = APIClient()
        response = client.post("/user/parent/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Upadate a Parent Users
    def test_parent_user_update(self):

        data = {
            "first_name": "Saif",
            "last_name": "Newaz",
            "street": "House no 177, North Vashantek",
            "city": "Dhaka",
            "state": "Dhaka",
            "zip_code": 1206
        }

        client = APIClient()
        self.parent.refresh_from_db()
        response = client.put("/user/parent/1/", data)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

    # Delete a Parent Users
    def test_parent_user_delete(self):

        client = APIClient()
        self.parent.refresh_from_db()
        response = client.delete("/user/parent/"+str(self.parent.id)+"/")
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)


# Api testing for POST method of child user
class ChildAPITests(APITestCase):

    # Setting up parent user
    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Saif",
            last_name="Newaz",
            street="Bou Bari Goli",
            city="Dhaka",
            state="Dhaka",
            zip_code=1206
        )

        self.child = Child.objects.create(
            parent=self.parent,
            first_name="Saif",
            last_name="Newaz",
        )

    # Get List of Child Users

    def test_child_list(self):

        client = APIClient()
        response = client.get("/user/child/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Create a Child Users

    def test_child_user_create(self):
        data = {
            "parent": self.parent.id,
            "first_name": "Saisha",
            "last_name": "Newaz",
        }

        client = APIClient()
        response = client.post("/user/child/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Update a Child Users
    def test_child_user_update(self):

        data = {
            "parent": self.parent.id,
            "first_name": "Updated",
            "last_name": "Newaz",
        }

        client = APIClient()
        self.child.refresh_from_db()
        response = client.put("/user/child/"+str(self.parent.id)+"/", data)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

    # Delete a Child Users
    def test_child_user_delete(self):

        client = APIClient()
        self.child.refresh_from_db()
        response = client.delete("/user/child/"+str(self.parent.id)+"/")
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)
