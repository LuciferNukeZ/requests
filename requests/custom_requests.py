import requests

class CustomSession(requests.Session):
    def request(self, method, url, **kwargs):
        print("Requesting URL:", url)
        print("Request parameters:", kwargs.get('params'))
        return super().request(method, url, **kwargs)
