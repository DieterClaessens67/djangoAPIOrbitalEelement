# serializers.py

from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import OrbitalElement


class OrbitalElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrbitalElement
        fields = ('id','Object', 'Epoch', 'TP', 'e',
                  'I', 'w', 'Node', 'q', 'Ql', 'P',
                  'MOID', 'A1', 'A2', 'A3', 'DT', 'ref',
                  'Object_name')

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user