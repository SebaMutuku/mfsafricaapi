from rest_framework import serializers

from MFSApp.models.models import DistanceModel
import numpy as np
class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
         ""
        )
        model = DistanceModel

    def calculateDistance(self, data):
        distance = 0
        return distance
