from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Task


@pytest.fixture
def common_user():
    user = User.objects.create_user(username="ali4", password="123")
    return user


@pytest.mark.django_db
class TestTasksApi:
    client = APIClient()

    def test_get_tasks_response_200_status(self, common_user):
        url = reverse("api-v1:task-list")
        self.client.force_authenticate(user=common_user)
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_task_response_201_status(self, common_user):
        url = reverse("api-v1:task-list")
        data = {"title": "string", "created_date": "2023-10-01"}
        self.client.force_authenticate(user=common_user)
        response = self.client.post(url, data)
        assert response.status_code == 201

    def test_patch_task_response_200_status(self, common_user):
        task = Task.objects.create(
            title="string", created_date="2023-10-01", user=common_user
        )
        url = reverse("api-v1:task-detail", kwargs={"pk": task.id})
        data = {"title": "string2"}
        self.client.force_authenticate(user=common_user)
        response = self.client.patch(url, data)
        assert response.status_code == 200
