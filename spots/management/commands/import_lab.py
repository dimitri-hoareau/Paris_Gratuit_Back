import logging
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from spots.models import LabHIV
import requests

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Imports labs spots data from an external API'

    def handle(self, *args, **options):
        self.fetch_and_import_records()

    def fetch_and_import_records(self):
        base_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/laboratoires-danalyses-medicales/records"
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
            print(data)
            total_count = data.get("total_count", 0)
            if number_of_iterations == 0:
                number_of_iterations = (total_count + limit - 1) // limit

            results = data.get("results", [])
            for record in results:
                try:

                    # Mettre à jour ou créer l'objet LabHIV
                    LabHIV.objects.update_or_create(
                        lab_id= record['code_cpam'],
                        defaults={
                            'lab_name': record['laboratoire'],
                            'address': record['adresse'],
                            'district': record['code_postal'],
                            'hours': record['horaires'],
                            'longitude': record['geo_point_2d']['lon'],
                            'latitude': record['geo_point_2d']['lat']
                        }
                    )
                    logger.info(LabHIV)
                except IntegrityError as e:
                    logger.error(f"Error inserting/updating record {record['code_cpam']}: {e}")
                    print("error for one LabHIV")

            offset += limit
            if offset >= number_of_iterations * limit:
                break

