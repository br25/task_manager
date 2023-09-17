from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    completion_status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ManyToManyField('Photo', blank=True, related_name='task_photos')

    def __str__(self):
        return self.title


class Photo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_photos')
    image = models.ImageField(upload_to='task_photos/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for Task: {self.task.title}"

