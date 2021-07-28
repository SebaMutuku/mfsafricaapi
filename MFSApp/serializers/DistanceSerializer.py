import math

from rest_framework import serializers
import ast
import itertools

from MFSApp.models import models
from MFSApp.models.models import PointsModel
import numpy as np


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'submittedpoints',
        )
        model = PointsModel

    def calculateDistance(self, data):
        x = ast.literal_eval(data['submittedpoints'])
        close_dist = float('inf')
        closest_points = ()
        for a, b in itertools.combinations(x, 2):
            diff_x = b[0] - a[0]
            diff_y = a[1] - b[1]
            result = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
            if result < close_dist:
                close_dist = result
                closest_points = (a, b)
                print("--------Saving data:: Received Point %s | closest points------ %s " % (
                    data['submittedpoints'], closest_points))
                entity = models.PointsModel.objects.create(submittedpoints=data['submittedpoints'],
                                                           closestpoints=closest_points)
                entity.save()
                print("Saved.....",entity.save())
                print("---Successfully saved entity-----")
        return closest_points
