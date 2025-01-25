from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from spots.models import OrganicWasteTrash
import requests
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Imports Organic Trash data from an external API'

    def handle(self, *args, **options):
        self.fetch_and_import_records()

    def fetch_and_import_records(self):
        base_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/dechets-menagers-points-dapport-volontaire-composteurs/records"
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
                print(record)
                try:
                    formatted_lon = record['geo_point_2d']['lon']
                    formatted_lat = record['geo_point_2d']['lat']
                    unique_id = f"{formatted_lon}_{formatted_lat}"

                    # Utilisation de update_or_create pour insérer ou mettre à jour une textile_trash
                    organic_trash, created = OrganicWasteTrash.objects.update_or_create(
                        trash_id=unique_id,
                        defaults={
                            'address': record['adresse'],
                            'district': record['code_postal'],
                            'spot_name': record['operateur'],
                            'longitude': formatted_lon,
                            'latitude': formatted_lat
                        }
                    )

                except IntegrityError as e:
                    print(f"Error inserting/updating record {unique_id}: {e}")
                    logger.error(f"Error inserting/updating record {unique_id}: {e}")

            offset += limit
            if offset >= number_of_iterations * limit:
                break
