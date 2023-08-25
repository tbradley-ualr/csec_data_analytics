from django.core.management.base import BaseCommand
import time

from csec_data_analytics_app.models import User, UserAddress


class Command(BaseCommand):
    help = 'Creates many documents in the MongoDB database.'

    def add_arguments(self, parser):
        parser.add_argument('--field',  type=str, default='last_name',  help='field to search on')
        parser.add_argument('--value', type=str, help='The value to search for')

    def handle(self, *args, **kwargs):
        field = kwargs['field']
        value = kwargs['value']

        start_time = time.time()
        results = User.objects(**{field: value})
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print(f"The duration of retrieving {len(results)} results on the field {field} is {execution_time} ms.")
