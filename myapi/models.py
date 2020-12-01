from django.db import models

# Create your models here.

class OrbitalElement(models.Model) :
    object = models.CharField(max_length=60)
    epoch = models.IntegerField()
    tp = models.FloatField()
    e = models.FloatField()
    i = models.FloatField()
    w = models.FloatField()
    node = models.FloatField()
    q = models.FloatField()
    ql = models.FloatField()
    p = models.FloatField()
    moid = models.FloatField()
    a1 = models.FloatField(blank=True, null=True, default=None)
    a2 = models.FloatField(blank=True, null=True, default=None)
    a3 = models.FloatField(blank=True, null=True, default=None)
    dt = models.FloatField(blank=True, null=True, default=None)
    ref = models.CharField(max_length=60)
    object_name = models.CharField(max_length=60)

    def __str__(self):
        return self.Object