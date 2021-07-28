from django.urls import reverse
from rest_framework import status

from MFSApp.models.models import PointsModel
from rest_framework.test import APITestCase


class ApiTest(APITestCase):
    model = PointsModel
    url=reverse("getpoints")
    def authorize_then_post(self):
        auth_bearer=self.client.credentials(HTTP_AUTHORIZATION="Basic bXNmYWZyaWNhOnRlc3QxMjM0Kio=")

    def test_fail_authorization(self):
        print("testing ...... fail_authorization")
        self.authorize_then_post()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_getPoints(self):
        print("testing ...... getPoints")
        data = self.model.objects.create(submittedpoints="(2,3),(4,7)", closestpoints="(2,3)")
        print("Data :: ",data)
        data.save()
        self.authorize_then_post()
        response = self.client.post(self.url,{"distance":"(2,2),(3,6)"})
        self.assertFalse(response.status_code, status.HTTP_200_OK)
