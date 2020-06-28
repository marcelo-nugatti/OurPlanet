from django.db import models

class WeightEarth(models.Model):
    name = models.CharField(max_length=250, null=True)
    weight = models.FloatField(null=True)

    def __str__(self):
        return str(self.name)




