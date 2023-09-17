from rest_framework import serializers
from .models import Task, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image', 'task']

class TaskSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'creation_date', 'due_date', 'priority', 'completion_status', 'photos']

    def get_photos(self, obj):
        photos = Photo.objects.filter(task=obj)
        return [self.context['request'].build_absolute_uri(photo.image.url) for photo in photos]

        
