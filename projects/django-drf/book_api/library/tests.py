from django.contrib.auth.models import User
from django.test import TestCase, tag
from django.urls import reverse
from rest_framework import status


class AuthenticationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="test", password="password")
        cls.test_user = User.objects.get(username="test")
        cls.endpoint_list_create = reverse("library:books-list-create")

    @tag("auth")
    def test_authenticated_user_get_request(self):
        self.client.login(username="test", password="password")
        response = self.client.get(self.endpoint_list_create)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag("auth")
    def test_unauthenticated_user_get_request(self):
        response = self.client.get(self.endpoint_list_create)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag("auth")
    def test_authenticated_user_post_request(self):
        self.client.force_login(self.test_user)
        data = {
            "id": 1,
            "title": "The Hitchhiker's Guide to the Galaxy",
            "author": "Douglas Adams",
            "publication_date": "1979-10-12",
            "isbn": "9780345391803",
            "summary": "A comedic science fiction adventure.",
        }
        response = self.client.post(
            path=self.endpoint_list_create,
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @tag("auth")
    def test_unauthenticated_user_post_request(self):
        data = {
            "id": 1,
            "title": "The Hitchhiker's Guide to the Galaxy",
            "author": "Douglas Adams",
            "publication_date": "1979-10-12",
            "isbn": "9780345391803",
            "summary": "A comedic science fiction adventure.",
        }
        response = self.client.post(
            path=self.endpoint_list_create, data=data, content_type="application/json"
        )

        # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # Without simple-jwt
        # With simple-jwt
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
