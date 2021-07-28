import math

from rest_framework import serializers

from MFSApp.models import models
from MFSApp.models.models import DistanceModel
import numpy as np
class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
         ""
        )
        model = DistanceModel

    def calculateDistance(self, data):
        model_data=models.DistanceModel.objects.create(submitpoints=data['distance'],closestpoints="(2,2),(4,6)")
        model_data.save()
        print(model_data)
        distance = 0
        x1=3
        x2=5
        y1=9
        y2=19
        sum_x=x1+x2
        sum_y=y1+y2
        distance=math.sqrt(math.pow(sum_x,2)+math.pow(sum_y,2))
        return distance
