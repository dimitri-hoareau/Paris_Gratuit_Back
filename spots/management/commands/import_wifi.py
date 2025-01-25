import logging
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from spots.models import WifiSpot
import requests

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Imports wifi spots data from an external API'

    def handle(self, *args, **options):
        self.fetch_and_import_records()

    def fetch_and_import_records(self):
        base_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/sites-disposant-du-service-paris-wi-fi/records"
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

                    # Mettre à jour ou créer l'objet WifiSpot
                    WifiSpot.objects.update_or_create(
                        wifi_id= record['idpw'],
                        defaults={
                            'spot_name': record['nom_site'],
                            'address': record['arc_adresse'],
                            'district': record['cp'],
                            'state': record['etat2'] == 'Opérationnel',
                            'longitude': record['geo_point_2d']['lon'],
                            'latitude': record['geo_point_2d']['lat']
                        }
                    )
                    logger.info(WifiSpot)
                except IntegrityError as e:
                    logger.error(f"Error inserting/updating record {record['idpw']}: {e}")
                    print("error for one wifispot")

            offset += limit
            if offset >= number_of_iterations * limit:
                break

