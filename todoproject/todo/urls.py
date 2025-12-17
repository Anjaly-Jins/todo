from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),          # List page
    path('todo/<int:id>/', views.todo_detail, name='todo_detail'),  # Detail page
    path('todo/<int:id>/edit/', views.edit_todo, name='edit_todo'),
    path('todo/<int:id>/delete/', views.delete_todo, name='delete_todo'),
    path('add/', views.add_todo, name='add_todo'),
]
