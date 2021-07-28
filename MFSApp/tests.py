from django.urls import reverse
from rest_framework import status

from MFSApp.models.models import PointsModel
from rest_framework.test import APITestCase


class ApiTest(APITestCase):
    model = PointsModel
    url = reverse("getpoints")

    def authorize_then_post(self):
        auth="bXNmYWZyaWNhOnRlc3QxMjM0Kio="
        auth_bearer = self.client.credentials(HTTP_AUTHORIZATION=f"Basic {auth}")

    def test_fail_authorization(self):
        print("--------testing fail_authorization-------")
        self.authorize_then_post()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_getPoints(self):
        print("--------testing getPoints-----------")
        self.authorize_then_post()
        data = self.model.objects.create(submittedpoints="(1,6),(9,19),(8,5)", closestpoints="(1,6),(8,5)")
        data.save()
        response = self.client.post(self.url, {"submittedpoints": "(1,6),(9,19),(8,5)"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
