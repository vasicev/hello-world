from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import TaskSerializers, TagSerializers
from .models import Task, Tag
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'active']

class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']