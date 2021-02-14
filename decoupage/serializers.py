from rest_framework import serializers
from .models import Region, Department, Town


class TownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = ['name']


class DepartmentSerializer(serializers.ModelSerializer):

    towns = TownSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['name', 'code_ansd', 'area', 'towns']


class RegionSerializer(serializers.ModelSerializer):

    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ['name', 'code_iso', 'code_ansd', 'area', 'departments']
