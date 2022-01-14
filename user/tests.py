# from django.test import TestCase
# from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import *


# Api testing for Parent user
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
    def test_get_parents_list(self):
        client = APIClient()
        response = client.get("/user/parent/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Create a Parent User
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

    # Upadate a Parent User
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
        response = client.put("/user/parent/"+str(self.parent.id)+"/", data)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

    # Delete a Parent User
    def test_parent_user_delete(self):

        client = APIClient()
        self.parent.refresh_from_db()
        response = client.delete("/user/parent/"+str(self.parent.id)+"/")
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)


# Api Testing for Child user
class ChildAPITests(APITestCase):

    # Setting up Parent User
    def setUp(self):
        # Setting up Parent User
        self.parent = Parent.objects.create(
            first_name="Hmmm",
            last_name="Ohhh",
            street="Bou Bari Goli",
            city="Dhaka",
            state="Dhaka",
            zip_code=1206
        )

        # Setting up Child User
        self.child = Child.objects.create(
            parent=self.parent,
            first_name="Saif",
            last_name="Newaz",
        )

    # Get List of Child Users

    def test_get_children_list(self):

        client = APIClient()
        response = client.get("/user/child/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Create a Child User

    def test_child_user_create(self):
        data = {
            "parent": self.parent.id,
            "first_name": "Saisha2",
            "last_name": "Newaz",
        }

        client = APIClient()
        response = client.post("/user/child/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Update a Child User
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

    # Delete a Child User
    def test_child_user_delete(self):

        client = APIClient()
        self.child.refresh_from_db()
        response = client.delete("/user/child/"+str(self.parent.id)+"/")
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)
