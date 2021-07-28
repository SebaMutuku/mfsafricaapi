from django.db import models


class DistanceModel(models.Model):
    submitpoints = models.CharField(max_length=4000,unique=True, null=True)
    closestpoints = models.CharField(max_length=4000)

    def __str__(self):
        return self.points
