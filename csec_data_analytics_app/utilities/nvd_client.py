import os
import requests
import json
from datetime import datetime, timedelta


class NVDClient:
    MAX_RESULTS_PER_REQUEST = 2000

    def __init__(self):
        to_date = datetime.utcnow()
        from_date = to_date - timedelta(days=120)
        self.api_url = f'https://services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate={from_date.isoformat()}&' \
                       f'lastModEndDate={to_date.isoformat()}'
        nvd_api_key = os.environ.get('NVD_API_KEY')
        self.header = {'apikey': nvd_api_key}
        self.cves = []

    def run(self):
        next_index = 0
        fetch_next = True
        while fetch_next:
            fetch_next, next_index = self._fetch_vulnerabilities(start_index=next_index)

    def _fetch_vulnerabilities(self, start_index=0):
        """
        Fetch vulnerabilities starting from the provided index.

        Args:
        - start_index (int): The index to start fetching from.

        Returns:
        - tuple(bool, int): A tuple containing a boolean indicating if more vulnerabilities
                            should be fetched, and the next index to start from.
        """
        response = requests.get(f"{self.api_url}&startIndex={start_index}", headers=self.header)
        if response.status_code != 200:
            response.raise_for_status()

        returned_content = json.loads(response.content)
        self.cves += returned_content['vulnerabilities']
        next_index = returned_content['startIndex'] + self.MAX_RESULTS_PER_REQUEST
        fetch_next = True if next_index < returned_content['totalResults'] else False
        return fetch_next, next_index
