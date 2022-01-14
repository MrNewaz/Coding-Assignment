# from django.test import TestCase
# from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..models import *


# Api testing for Parent user
class ParentAPITests(APITestCase):

    # Setting up parent user
    def setUp(self):
        self.parent = Parent.objects.create(
            first_name="Saif",
            last_name="Newaz",
            street="Bou Baazar",
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
            "street": "Bou Baazar",
            "city": "Dhaka",
            "state": "Dhaka",
            "zip_code": 1206
        }

        client = APIClient()
        response = client.post("/user/parent/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Upadate a Parent User by id(pk)
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

    # Delete a Parent User by id(pk)
    def test_parent_user_delete(self):

        client = APIClient()
        self.parent.refresh_from_db()
        response = client.delete("/user/parent/"+str(self.parent.id)+"/")
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)
