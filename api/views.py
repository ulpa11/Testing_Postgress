import re
from django.shortcuts import render
from .models import BusSatusData
from .serializer import BusSatusDataSerializer
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
class BusSatusDataViewSet(viewsets.ModelViewSet):
    queryset = BusSatusData.objects.all()
    serializer_class = BusSatusDataSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
        