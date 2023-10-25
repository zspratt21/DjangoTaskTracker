from django.test import TestCase
from App.models import Task


class TaskModelTests(TestCase):

    def test_model_creation(self):
        task = Task.objects.create(name="Test Task", isCompleted=False)
        self.assertEqual(Task.objects.count(), 1)
