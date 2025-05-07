from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test", password="password")

    def test_only_authenticated_users_upload_data(self):
        # user = User.objects.get(username="test")
        # self.client.force_login(user)
        self.client.login(username="test", password="password")
        response = self.client.get(reverse("library:books-lc"))

        self.assertEqual(response.status_code, 200)
