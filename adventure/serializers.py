from rest_framework import serializers

from adventure import models


class JourneySerializer(serializers.Serializer):
    name = serializers.CharField()
    passengers = serializers.IntegerField()


class VehicleTypeSerializer(serializers.Serializer):
    name = serializers.CharField()
    capacity = serializers.IntegerField()


class VehicleSerializer(serializers.Serializer):
    name = serializers.CharField()
    passengers = serializers.IntegerField()
    vehicle_type = VehicleTypeSerializer(many=False, read_only=True)
    number_plate = serializers.CharField()
    fuel_efficiency = serializers.DecimalField(max_digits=6, decimal_places=2)
    fuel_tank_size = serializers.DecimalField(max_digits=6, decimal_places=2)


class ServiceAreaSerializer(serializers.Serializer):
    kilometer = serializers.IntegerField()
    gas_price = serializers.IntegerField()
