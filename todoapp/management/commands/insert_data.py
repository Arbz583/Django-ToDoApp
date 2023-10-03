from django.core.management.base import BaseCommand
from faker import Faker
import random
from django.contrib.auth.models import User
from todoapp.models import Task


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(
            username=self.fake.user_name(), password="Test@123456"
        )
        for _ in range(5):
            Task.objects.create(
                user=user,
                title=self.fake.paragraph(nb_sentences=1),
                complete=random.choice([True, False]),
            )
