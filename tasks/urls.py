from django.urls import path
from . import views

urlpatterns = [
    # Task Class-based API URLs
    path('tasks/', views.TaskListAPIView.as_view(), name='task-list'),
    path('tasks/create/', views.TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', views.TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', views.TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteAPIView.as_view(), name='task-delete'),

    # Photos Class-based API URLs
    path('photos/', views.PhotoListCreateView.as_view(), name='photo-list-create'),
    path('photos/<int:pk>/', views.PhotoDetailView.as_view(), name='photo-detail'),

    # Task Function-based API URLs
    path('', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('<int:pk>/', views.task_detail, name='task-detail'),
    path('<int:pk>/update/', views.task_update, name='task-update'),
    path('<int:pk>/delete/', views.task_delete, name='task-delete'),
]
