from charts.settings import BASE_DIR
import csv
from django.core.management.base import BaseCommand, CommandError

from app1.models import SuicideCase

def build_database_entities(list_of_rows):
    entites = {}
    for row in list_of_rows:
        country = row['country']
        entites.setdefault(str(country),[])
        entites[country] = entites.get(country) + [{"year" : row['year'],"suicides_no": row['suicides_no']}]
        print(entites[country])
        
    for country in entites:
        data_list = entites.get(country)

class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = BASE_DIR / 'data/master.csv'
        with open(file_path, 'r') as csv_file:
            file_header = ['country', 'year', 'suicides_no']
            reader = csv.DictReader(csv_file, fieldnames=file_header)
            next(reader)
            build_database_entities([row for row in reader])
