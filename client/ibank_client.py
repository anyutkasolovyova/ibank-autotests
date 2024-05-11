import requests


class IBankClient:
    def http_get(self, url):
        requests.get(url=url)
