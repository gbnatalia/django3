from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Get User by id."

    def add_arguments(self, parser):
        #parser.add_argument('id', type=int, help='User ID')
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        #id = kwargs['id']
        #user = User.objects.get(id=id)
        id = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
