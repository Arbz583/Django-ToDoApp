from celery import shared_task
from django.contrib.auth.models import User
from .models import Task

users=User.objects.all()

@shared_task
def delete_completed_task():
    for user in users:
        completed_tasks=Task.objects.filter(user=user, complete=True)
        completed_tasks.delete()