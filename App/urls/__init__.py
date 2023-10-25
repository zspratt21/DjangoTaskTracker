from django.urls import path, include

urlpatterns = [
    path('', include('App.urls.welcome_urls')),
    path('', include('App.urls.task_urls')),
]
