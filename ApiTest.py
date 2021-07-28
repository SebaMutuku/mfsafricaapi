from unittest import TestCase

from crypto.SelfTest.Hash.test_SHA3_224 import APITest
from django.urls import reverse
from rest_framework import status

from MFSApp.models.models import DistanceModel
from rest_framework.test import APITestCase


class ApiTest(APITestCase):
    model = DistanceModel

    def readRequest(self):
        url = reversed("getpoints")
        data = self.model.objects.create(points="(2,2),(4,7)", distance=100)
        data.save()
        response = self.client.post(url, format='json')
        self.assertEqual(response, status.HTTP_200_OK)
