from rest_framework import serializers
from .models import Tag, Task

class TaskSerializers(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'created')