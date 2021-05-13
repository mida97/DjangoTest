from django.core.management.base import BaseCommand, CommandError
from users.models import User

class Command(BaseCommand):
    newuser = User(
        email='user1@email.com',
        username='user1',
        is_superuser=True,
    )
    newuser.set_password(raw_password='init123')