from django.urls import reverse
from rest_framework import status

from MFSApp.models.models import DistanceModel
from rest_framework.test import APITestCase


class ApiTest(APITestCase):
    model = DistanceModel
    url=reverse("getpoints")
    def authorize_then_post(self):
        auth_bearer=self.client.credentials(HTTP_AUTHORIZATION="Basic bXNmYWZyaWNhOnRlc3QxMjM0Kio")


    def test_getPoints(self):
        print("testing ......")
        data = self.model.objects.create(points="(2,2),(4,7)", distance=100)
        print(data)
        data.save()
        self.authorize_then_post()
        response = self.client.post(self.url,{"distance":"(2,2),(3,6)"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
