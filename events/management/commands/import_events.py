from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from events.models import Event
import requests
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Imports events data from an external API'

    def handle(self, *args, **options):
        self.fetch_and_import_records()

    def fetch_and_import_records(self):
        base_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/que-faire-a-paris-/records"
        offset = 0
        limit = 100
        number_of_iterations = 0

        while True:
            url = f"{base_url}?limit={limit}&offset={offset}"
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.RequestException as e:
                logger.error(f"Failed to fetch data: {e}")
                raise CommandError(f"API request failed: {e}")

            data = response.json()
            total_count = data.get("total_count", 0)
            if number_of_iterations == 0:
                number_of_iterations = (total_count + limit - 1) // limit

            results = data.get("results", [])
            for record in results:
                price_type = record.get('price_type', '')
                if price_type and price_type.lower() not in ['gratuit', 'gratuit sous condition']:
                    continue 

                print(record)
                try:
                    lat_lon = record.get('lat_lon', {})
                    latitude = lat_lon.get('lat') if lat_lon else None
                    longitude = lat_lon.get('lon') if lat_lon else None


                    # Utilisation de update_or_create pour insérer ou mettre à jour une textile_trash
                    recyceventling, created = Event.objects.update_or_create(
                        event_id=record['id'],
                        defaults={
                            'url': record.get('url', ''),
                            'title': record.get('title', 'No Title'),
                            'lead_text': record.get('lead_text', ''),
                            'description': record.get('description'),
                            'date_start': record.get('date_start'),
                            'date_end': record.get('date_end'),
                            'occurrences': record.get('occurrences'),
                            'date_description': record.get('date_description'),
                            'cover_url': record.get('cover_url'),
                            'cover_alt': record.get('cover_alt'),
                            'cover_credit': record.get('cover_credit'),
                            'tags': record.get('tags', []),
                            'address_name': record.get('address_name', ''),
                            'address_street': record.get('address_street', ''),
                            'address_zipcode': record.get('address_zipcode', ''),
                            'address_city': record.get('address_city', ''),
                            'price_type': price_type,
                            'price_detail': record.get('price_detail', ''),
                            'latitude': latitude,
                            'longitude': longitude
                        }
                    )

                except IntegrityError as e:
                    print(f"Error inserting/updating record {record['id']}: {e}")
                    logger.error(f"Error inserting/updating record {record['id']}: {e}")

            offset += limit
            if offset >= number_of_iterations * limit:
                break
