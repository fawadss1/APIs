from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from . import Serializer
from . import models


# @api_view(['GET', 'POST'])
@csrf_exempt
def index(request):
    if request.method == 'GET':
        std = models.Student.objects.all()
        crs = models.Course.objects.all()
        inst = models.Instructor.objects.all()
        stdSerializer = Serializer.StdSerliazer(std, many=True)
        crsSerializer = Serializer.CrsSerliazer(crs, many=True)
        instSerializer = Serializer.InstSerliazer(inst, many=True)
        var = stdSerializer.data, crsSerializer.data, instSerializer.data
        return JsonResponse(var, safe=False)


@csrf_exempt
def students(request):
    if request.method == 'GET':
        std = models.Student.objects.all()
        stdSerializer = Serializer.StdSerliazer(std, many=True)
        return JsonResponse(stdSerializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Serializer.StdSerliazer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_details(request, pk):
    try:
        std = models.Student.objects.get(pk=pk)
    except models.Student.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        stdSerializer = Serializer.StdSerliazer(std)
        return JsonResponse(stdSerializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Serializer.StdSerliazer(std, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        std.delete()
        return JsonResponse(status=204)
