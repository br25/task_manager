from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, status, filters
from rest_framework.response import Response
from .models import Task, Photo
from .serializers import TaskSerializer, PhotoSerializer
from .forms import TaskForm, PhotoForm

# RestAPI View
class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by creation_date
        creation_date = self.request.query_params.get('creation_date', None)
        if creation_date:
            queryset = queryset.filter(creation_date=creation_date)

        # Filter by due_date
        due_date = self.request.query_params.get('due_date', None)
        if due_date:
            queryset = queryset.filter(due_date=due_date)

        # Filter by priority
        priority = self.request.query_params.get('priority', None)
        if priority:
            queryset = queryset.filter(priority=priority)

        # Filter by completion_status
        completion_status = self.request.query_params.get('completion_status', None)
        if completion_status:
            queryset = queryset.filter(completion_status=completion_status)

        return queryset

class TaskCreateAPIView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskDetailAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteAPIView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


# Html connection with forms
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            photos = request.FILES.getlist('photos')
            for photo in photos:
                Photo.objects.create(task=task, image=photo)
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_update.html', {'form': form, 'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')
    return render(request, 'task_delete.html', {'task': task})


# Photo
def task_photos(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    photos = task.photos.all()
    return render(request, 'task_photos.html', {'task': task, 'photos': photos})