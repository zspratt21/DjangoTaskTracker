from django.urls import path
from App import views

urlpatterns = [
    path('api/Tasks', views.TaskListCreate.as_view(), name='task-list-create'),
    path('api/Tasks/<int:pk>', views.TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
]
