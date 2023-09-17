from django.contrib import admin
from .models import Task, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'due_date', 'completion_status', 'user')
    list_filter = ('priority', 'completion_status')
    search_fields = ('title', 'description')
    inlines = [PhotoInline]
    date_hierarchy = 'due_date'
    ordering = ('priority',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('task', 'image', 'upload_date')
    list_filter = ('task',)
    date_hierarchy = 'upload_date'
