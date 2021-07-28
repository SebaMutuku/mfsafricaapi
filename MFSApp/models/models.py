from django.db import models


class DistanceModel(models.Model):
    distance=models.IntegerField()
    points=models.CharField(max_length=400)

