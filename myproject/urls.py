from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line tells Django: "For any URLs, go check the todo app"
    path('', include('todo.urls')),
]