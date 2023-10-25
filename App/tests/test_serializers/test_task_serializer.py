from django.test import TestCase
from App.serializers import TaskSerializer


class TaskSerializerTests(TestCase):

    def test_serializer_valid_data(self):
        data = {
            "name": "Test Task",
            "isCompleted": False
        }
        serializer = TaskSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        data = {
            "name": "",  # empty name
            "isCompleted": False
        }
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())
