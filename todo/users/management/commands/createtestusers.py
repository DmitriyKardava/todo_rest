import os
import json
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from todo.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Create test users from testusers.json'

    def handle(self, *args, **kwargs):
        users = json.load(open(os.path.join(BASE_DIR, 'json/testusers.json')))
        User = get_user_model()
        for user in users:
            if not User.objects.filter(username=user['username']).exists():
                User.objects.create(
                    username=user['username'],
                    email=user['email'],
                    password=make_password(user['password']),
                    is_staff=user['is_staff'],
                    is_superuser=user['is_superuser']
                )
