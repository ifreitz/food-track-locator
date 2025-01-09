from rest_framework import serializers
from api.models import FoodTruck


class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = '__all__'
