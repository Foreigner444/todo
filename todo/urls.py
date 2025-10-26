from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('unmark_completed/<int:pk>/', views.unmark_completed, name='unmark_completed'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task')
]