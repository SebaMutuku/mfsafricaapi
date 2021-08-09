import math

from rest_framework import serializers
import ast
import itertools

from MFSApp.models import models
from MFSApp.models.models import PointsModel


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
            distance = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))
            if distance < close_dist:
                close_dist = distance
                closest_points = (a, b)
        print("--------Saving data:: Received Point %s | closest points------ %s -----distance %s" % (
            data['submittedpoints'], closest_points, distance))
        entity = models.PointsModel.objects.create(submittedpoints=data['submittedpoints'],
                                                   closestpoints=closest_points)
        entity.save()
        print("---Successfully saved entity-----")
        return str(closest_points)
