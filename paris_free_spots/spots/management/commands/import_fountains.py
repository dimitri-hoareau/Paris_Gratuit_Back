import logging
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from spots.models import DrinkingFountain
import requests

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Imports fountain data from an external API'

    def handle(self, *args, **options):
        self.fetch_and_import_records()

    def fetch_and_import_records(self):
        base_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/fontaines-a-boire/records"
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
                try:
                    # Déterminer le numéro de voirie à inclure dans l'adresse
                    no_voirie = record.get('no_voirie_impair') or record.get('no_voirie_pair') or ''
                    if no_voirie:
                        no_voirie += ' '  # Ajouter un espace après le numéro s'il existe

                    # Construire l'adresse complète
                    address = f"{no_voirie}{record['voie']}, {record['commune']}".strip()

                    # Mettre à jour ou créer l'objet DrinkingFountain
                    DrinkingFountain.objects.update_or_create(
                        fountain_id= record['gid'],
                        defaults={
                            'object_type': record['type_objet'],
                            'address': address,
                            'district': record['commune'].split()[-1],
                            'available': record['dispo'] == 'OUI',
                            'longitude': record['geo_point_2d']['lon'],
                            'latitude': record['geo_point_2d']['lat']
                        }
                    )
                    logger.info(DrinkingFountain)
                except IntegrityError as e:
                    logger.error(f"Error inserting/updating record {record['gid']}: {e}")

            offset += limit
            if offset >= number_of_iterations * limit:
                break
