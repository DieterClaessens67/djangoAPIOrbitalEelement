from django.db import models

# Create your models here.

class OrbitalElement(models.Model) :
    Object = models.CharField(max_length=60)
    Epoch = models.IntegerField()
    TP = models.FloatField()
    e = models.FloatField()
    I = models.FloatField()
    w = models.FloatField()
    Node = models.FloatField()
    q = models.FloatField()
    Ql = models.FloatField()
    P = models.FloatField()
    MOID = models.FloatField()
    A1 = models.FloatField(blank=True, null=True, default=None)
    A2 = models.FloatField(blank=True, null=True, default=None)
    A3 = models.FloatField(blank=True, null=True, default=None)
    DT = models.FloatField(blank=True, null=True, default=None)
    ref = models.CharField(max_length=60)
    Object_name = models.CharField(max_length=60)

    def __str__(self):
        return self.Object