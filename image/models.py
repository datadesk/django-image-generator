from django.db import models

class State(models.Model):
    """
    A state, with associated SVG path and unemployment rate
    """
    name = models.CharField(max_length=200)
    postal = models.CharField(max_length=2)
    unemployment_rate = models.FloatField()
    svg_path = models.TextField()
    color = models.CharField(max_length=7)
