from django.db import models


class PointsModel(models.Model):
    submittedpoints = models.CharField(max_length=4000)
    closestpoints = models.CharField(max_length=4000)

    def __str__(self):
        return self.submittedpoints
