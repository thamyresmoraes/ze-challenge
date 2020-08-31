from typing import Dict

import requests
from requests import Response


class OpenWeatherMap:
    def __init__(self, userdata: Dict[str, str]):
        self.api_url = userdata.get('api_url')
        self.token_api = userdata.get('APPID')

    def day_temperature(self, id) -> Response:    
        payload = {'id':id, 'APPID':self.token_api}
        resp = requests.get(self.api_url, params=payload)

        return resp
