from django.urls import path
from App import views

urlpatterns = [
    path('api/tasks/', views.TaskListCreate.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
]
