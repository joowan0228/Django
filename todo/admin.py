from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'is_completed', 'created_at', 'modified_at')
    list_filter = ('is_completed', 'start_date', 'end_date')
    search_fields = ('title', 'description')
