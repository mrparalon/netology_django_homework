from django.contrib.auth.management.commands.createsuperuser import Command


def validate_password(password, user=None, password_validators=None):
    return None


class Command(Command):
    help = 'Create superuser with not strong password'
