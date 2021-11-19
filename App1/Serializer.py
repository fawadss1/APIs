from rest_framework import serializers
from . import models


class StdSerliazer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        # fields = ('Name', 'Father_Name')
        fields = '__all__'
