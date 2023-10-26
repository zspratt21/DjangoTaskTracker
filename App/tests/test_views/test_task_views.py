from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from App.models import Task


class TasksControllerTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.task1 = Task.objects.create(name="Task 1", isCompleted=False)
        self.task2 = Task.objects.create(name="Task 2", isCompleted=True)

    def test_get_tasks_returns_all_tasks(self):
        response = self.client.get(reverse('task-list-create'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Task 1')

    def test_get_task_item_returns_task_item_when_it_exists(self):
        response = self.client.get(reverse('task-retrieve-update-destroy', args=[self.task1.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Task 1')

    def test_get_task_item_returns_not_found_when_it_does_not_exist(self):
        response = self.client.get(
            reverse('task-retrieve-update-destroy', args=[0]))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_task_item_returns_bad_request_when_ids_do_not_match(self):
        response = self.client.put(
            reverse('task-retrieve-update-destroy', args=[self.task1.id]),
            {'id': self.task2.id, 'name': 'Task 2', 'isCompleted': True}
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_task_item_returns_created_when_successful(self):
        data = {'name': 'Task 3', 'isCompleted': False}
        response = self.client.post(reverse('task-list-create'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def tearDown(self):
        pass
