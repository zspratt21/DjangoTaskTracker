from rest_framework import generics, status
from rest_framework.response import Response

from App.models import Task
from App.serializers import TaskSerializer


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the ID in the URL matches the ID in the request body and return a 400 if they don't match.
        if 'id' not in request.data or int(request.data['id']) != instance.id:
            return Response(
                {"detail": "Mismatched IDs or ID not included in request body."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super(TaskRetrieveUpdateDestroy, self).update(request, *args, **kwargs)