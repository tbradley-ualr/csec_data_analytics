import requests
from mongoengine import connect
from csec_data_analytics_app.models import Vulnerability

class NVDDataImporter:
    def __init__(self, api_base_url, mongo_uri):
        self.api_base_url = api_base_url
        self.mongo_uri = mongo_uri

    def fetch_cve_data(self, year):
        url = f"{self.api_base_url}/nvd/vuln/data-feed/json/cve/{year}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch CVE data for {year}. Error {response.status_code}: {response.text}")

    def import_cve_data_to_mongodb(self, year):
        cve_data = self.fetch_cve_data(year)

        connect(db='django-mongo.vulnerabilities', host=self.mongo_uri)

        for cve_item in cve_data['CVE_Items']:
            cve_id = cve_item['cve']['CVE_data_meta']['ID']
            description = cve_item['cve']['description']['description_data'][0]['value']
            cpe_configurations = [config['cpe_match']['cpe23Uri'] for config in cve_item['configurations']['nodes']]
            cwes = [cwe['value'] for cwe in cve_item['cve']['problemtype']['problemtype_data'][0]['descriptions']]

            cvss_base_score = cve_item['impact']['baseMetricV3']['cvssV3']['baseScore']
            cvss_exploitability_score = cve_item['impact']['baseMetricV3']['exploitabilityScore']
            cvss_impact_score = cve_item['impact']['baseMetricV3']['impactScore']
            cvss_vector = cve_item['impact']['baseMetricV3']['cvssV3']['vectorString']
            cvss_version = '3.1'

            vulnerability = Vulnerability(
                cve_id=cve_id,
                description=description,
                cpe_configurations=cpe_configurations,
                cwes=cwes,
                cvss_attributes={
                    'base_score': cvss_base_score,
                    'exploitability_score': cvss_exploitability_score,
                    'impact_score': cvss_impact_score,
                    'vector': cvss_vector,
                    'version': cvss_version
                }
            )

            vulnerability.save()

if __name__ == "__main__":
    api_base_url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
    mongo_uri = 'mongodb://localhost:27017/django-mongo.vulnerabilities'
    year_to_import = 2023  # Replace with the desired year

    nvd_importer = NVDDataImporter(api_base_url, mongo_uri)
    nvd_importer.import_cve_data_to_mongodb(year_to_import)
