from django.core.management.base import BaseCommand
import json
from datetime import datetime
from dashboard_app.models import DataEntry


class Command(BaseCommand):
    help = 'Load data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

            for entry in json_data:
                data_entry = DataEntry()

                data_entry.sector = entry["sector"]
                data_entry.topic = entry["topic"]
                data_entry.insight = entry["insight"]
                data_entry.url = entry["url"]
                data_entry.region = entry["region"]
                data_entry.country = entry["country"]
                data_entry.pestle = entry["pestle"]
                data_entry.source = entry["source"]
                data_entry.title = entry["title"]

                # Parse the date strings using the correct format
                published_str = entry["published"]
                added_str = entry["added"]
                try:
                    published = datetime.strptime(published_str, "%B, %d %Y %H:%M:%S")
                    data_entry.published = published
                except ValueError:
                    self.stdout.write(self.style.ERROR(f'Invalid published date format: {published_str}'))
                
                try:
                    added = datetime.strptime(added_str, "%B, %d %Y %H:%M:%S")
                    data_entry.added = added
                except ValueError:
                    self.stdout.write(self.style.ERROR(f'Invalid added date format: {added_str}'))

                data_entry.intensity = entry["intensity"]
                data_entry.start_year = entry["start_year"]
                data_entry.end_year = entry["end_year"]
                data_entry.impact = entry["impact"]
                data_entry.relevance = entry["relevance"]
                data_entry.likelihood = entry["likelihood"]

                data_entry.save()

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
