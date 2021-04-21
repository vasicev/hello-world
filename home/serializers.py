from rest_framework import serializers
from .models import Tag, Task

class TaskSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

class TagSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'