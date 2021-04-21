from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import TaskSerializers, TagSerializers
from .models import Task, Tag
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

# @api_view(['GET'])
# def index(request):
#     # return HttpResponse("Hello World!")
#     tasks = Task.objects.all()
#     serializers = TaskSerializers(tasks, many=True)
#     return Response(serializers.data)

class TaskViewSet(viewsets.ModelViewSet):

    # def list(self, request):
    #     task = Task.objects.all()
    #     serializer = TaskSerializers(task, many=True)
    #     return Response(serializer.data)

    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    # def get_queryset(self):
    #     return Task.objects.filter(tags=6).filter(tags=7)

class TagViewSet(viewsets.ModelViewSet):

    # def list(self, request):
    #     task = Task.objects.all()
    #     serializer = TaskSerializers(task, many=True)
    #     return Response(serializer.data)

    queryset = Tag.objects.all()
    serializer_class = TagSerializers