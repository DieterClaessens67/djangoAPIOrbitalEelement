from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import OrbitalElementSerializer
from .models import OrbitalElement
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class OrbitalElementViewSet(viewsets.ModelViewSet):
     permission_classes = (IsAuthenticatedOrReadOnly,)
     queryset = OrbitalElement.objects.all().order_by('Object')
     serializer_class = OrbitalElementSerializer

