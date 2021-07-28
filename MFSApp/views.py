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
        # print("Username >>>>> %s Password >>>>> %s"%(username,password))
        if username != settings.BASIC_USERNAME and password != settings.BASIC_PASSWORD:
            return Response({"Message": "Authorization Failed"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.data.get("distance").split(","))
            resp = serializer.calculateDistance(request.data)
            print("Response ", resp)
            return Response({"Points":resp}, status=status.HTTP_200_OK)
        return Response({"Error":"Invalid"}, status=status.HTTP_401_UNAUTHORIZED)
