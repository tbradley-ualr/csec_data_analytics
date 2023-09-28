from django.core.management.base import BaseCommand
from csec_data_analytics_app.utilities.nvd_client import NVDClient
from django.core.management.base import BaseCommand
from csec_data_analytics_app.management.commands.nvd_data_importer import NVDDataImporter  # Replace with the actual path to your NVDDataImporter class



#class Command(BaseCommand):
 #   help = 'Describes what your command does.'

  #  def handle(self, *args, **kwargs):
   ##    nvd_client.run()

class Command(BaseCommand):
    help = 'Import CVE data from NVD API and store it in MongoDB'

    def add_arguments(self, parser):
        parser.add_argument('year', type=int, help='The year for which to import CVE data')

    def handle(self, *args, **options):
        year_to_import = options['year']
        nvd_importer = NVDDataImporter(
            api_base_url='https://services.nvd.nist.gov/rest/json/cves/2.0',
            mongo_uri='mongodb://localhost:27017/django-mongo.vulnerabilities'  # Replace with your MongoDB URI
        )
        nvd_importer.import_cve_data_to_mongodb(year_to_import)
        self.stdout.write(self.style.SUCCESS(f'Successfully imported CVE data for {year_to_import}'))
