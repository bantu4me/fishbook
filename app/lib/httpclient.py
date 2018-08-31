import requests


class HttpClient:

    @staticmethod
    def get(url, return_json=True):
        resp = requests.get(url)
        if resp.status_code != 200:
            return {} if return_json else ''
        return resp.json() if return_json else resp.text



