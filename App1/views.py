from django.http import JsonResponse
from rest_framework.response import responses
from django.shortcuts import get_object_or_404
from rest_framework import status
from . import Serializer
from . import models


def get(request):
    if request.method == 'GET':
        std = models.Student.objects.all()
        serializer = Serializer.StdSerliazer(std, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        pass
