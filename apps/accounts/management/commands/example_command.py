from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Add Dummy data'

    def handle(self, *args, **options):
        print('panda_jumper test')
