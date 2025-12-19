from django.shortcuts import render, redirect
from .models import TodoItem

# 1. Homepage View: Shows the list of items
def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

# 2. Add View: Creates a new item
def add_todo(request):
    if request.method == 'POST':
        # Get data from the form
        subject = request.POST.get('subject')
        notes = request.POST.get('notes')
        
        # Save it to the database
        new_item = TodoItem(subject=subject, notes=notes)
        new_item.save()
        
        # Go back to the homepage
        return redirect('index')
    
    # If it's a GET request, just show the form
    return render(request, 'todo/add_todo.html')

# 3. Delete View: Removes an item
def delete_todo(request, todo_id):
    # Find the specific item by its ID
    item = TodoItem.objects.get(id=todo_id)
    # Delete it
    item.delete()
    # Go back to the homepage
    return redirect('index')

# 4. Edit View: Updates an existing item
def edit_todo(request, todo_id):
    # Get the item we want to edit
    item = TodoItem.objects.get(id=todo_id)
    
    if request.method == 'POST':
        # Update the item with new data from the form
        item.subject = request.POST.get('subject')
        item.notes = request.POST.get('notes')
        item.save()
        # Go back to the homepage
        return redirect('index')
    
    # Show the edit page with the existing item data pre-filled
    return render(request, 'todo/edit_todo.html', {'item': item})
# 5. Detail View (The "View" Button)
def view_todo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    return render(request, 'todo/detail_todo.html', {'item': item})
def delete_todo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    
    if request.method == 'POST':
        # Only delete if the user clicked the "Confirm" button
        item.delete()
        return redirect('index')
        
    # Otherwise, show the confirmation page
    return render(request, 'todo/delete_todo.html', {'item': item})