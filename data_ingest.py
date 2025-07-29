# data_ingest.py
import requests

class DataIngest:
    def __init__(self, sources):
        self.sources = sources  # dict of name->URL

    def fetch(self):
        data = {}
        for name, url in self.sources.items():
            resp = requests.get(url)
            resp.raise_for_status()
            data[name] = resp.json()
        return data


