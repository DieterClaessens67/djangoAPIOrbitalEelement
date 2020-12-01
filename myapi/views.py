from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.authtoken.admin import User

from .serializers import OrbitalElementSerializer
from .models import OrbitalElement
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .serializers import UserSerialiser


class OrbitalElementViewSet(viewsets.ModelViewSet):
     permission_classes = (IsAuthenticatedOrReadOnly,)
     queryset = OrbitalElement.objects.all().order_by('object')
     serializer_class = OrbitalElementSerializer


class UserCreate(generics.CreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerialiser
     permission_classes = (AllowAny, )