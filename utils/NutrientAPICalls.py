import requests


class NutrientAPI:
    def __init__(self, api_key, configs):
        self.api_key = api_key
        self.configs = configs

    def getNutrient(self, query):
        api_url = self.configs['api']['nutrient']['baseURL'] + self.configs['api']['nutrient']['search']
        res = requests.get(api_url, params={'query': query, 'api_key': self.api_key})
        json_res = res.json()
        return json_res['foods'][0]['foodNutrients']




