from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import TaskSerializers
from .models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    # return HttpResponse("Hello World!")
    tasks = Task.objects.all()
    serializers = TaskSerializers(tasks, many=True)
    return Response(serializers.data)