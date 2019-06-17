from csv import DictReader

from django.core.management.base import BaseCommand
from phones.models import Phone
import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csv_file:
            reader = DictReader(csv_file, delimiter=';')
            for phone in reader:
                release_date = datetime.datetime.strptime(phone['release_date'],
                                                        '%Y-%m-%d')
                if phone['lte_exists'] == 'True':
                    lte_exists = True
                elif phone['lte_exists'] == 'False':
                    lte_exists = False
                db_phone = Phone(id=int(phone['id']),
                                 name=phone['name'],
                                 image=phone['image'],
                                 price=int(phone['price']),
                                 release_date=release_date,
                                 lte_exists=lte_exists)
                db_phone.save()
            print('All phones added to DB')