from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            default='admin',
            help='Superuser username'
        )
        parser.add_argument(
            '--email',
            default='admin@example.com',
            help='Superuser email'
        )
        parser.add_argument(
            '--password',
            default='admin123',
            help='Superuser password'
        )

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username']
        email = options['email']
        password = options['password']

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(
                self.style.SUCCESS(f'Superuser {username} created successfully')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Superuser {username} already exists')
            )