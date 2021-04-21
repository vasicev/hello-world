from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import TaskSerializers, TagSerializers
from .models import Task, Tag
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializers