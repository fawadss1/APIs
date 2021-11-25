from rest_framework import serializers
from . import models


class StdSerliazer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        # fields = ('Name', 'Father_Name')
        fields = '__all__'


class CrsSerliazer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        # fields = ('Name')
        fields = '__all__'


class InstSerliazer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        # fields = ('Name',)
        fields = '__all__'
