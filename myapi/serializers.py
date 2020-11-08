# serializers.py

from rest_framework import serializers

from .models import OrbitalElement


class OrbitalElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrbitalElement
        fields = ('id','Object', 'Epoch', 'TP', 'e',
                  'I', 'w', 'Node', 'q', 'Ql', 'P',
                  'MOID', 'A1', 'A2', 'A3', 'DT', 'ref',
                  'Object_name')