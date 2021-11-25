from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from . import Serializer
from . import models


@csrf_exempt
def index(request):
    if request.method == 'GET':
        std = models.Student.objects.all()
        serializer = Serializer.StdSerliazer(std, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Serializer.StdSerliazer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
