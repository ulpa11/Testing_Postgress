from rest_framework import serializers
from .models import BusSatusData

class BusSatusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSatusData
        fields = "__all__"
