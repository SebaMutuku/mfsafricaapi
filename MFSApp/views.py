import base64
from logging import raiseExceptions

from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from MFSApp.serializers.DistanceSerializer import ActionSerializer
from MfsAfricaApi import settings


class DistanceView(views.APIView):
    serializer_class = ActionSerializer

    def post(self, request):
        authorization = request.META.get('HTTP_AUTHORIZATION', '').replace("Basic", "").replace("\\s", "")
        username = base64.b64decode(authorization).decode("utf-8").split(":")[0]
        password = base64.b64decode(authorization).decode("utf-8").split(":")[1]
        print("------Received Request %s----- \n------authorization string %s------" % (request.data, authorization))
        if username != settings.BASIC_USERNAME and password != settings.BASIC_PASSWORD:
            return Response({"Detail": "Invalid username/password."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            resp = serializer.calculateDistance(request.data)
            print("--------Response written---- ", resp)
            return Response({"closest_points": resp}, status=status.HTTP_200_OK)
        return Response({"Error": "Invalid"}, status=status.HTTP_401_UNAUTHORIZED)
