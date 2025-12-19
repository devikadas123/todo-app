from django.contrib import admin
from .models import TodoItem

# This tells the Admin panel to show your TodoItem database
admin.site.register(TodoItem)