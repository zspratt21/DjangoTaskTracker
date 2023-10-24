from django.urls import path, include

urlpatterns = [
    path('', include('App.urls.task_urls')),
]
