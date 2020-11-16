from decouple import config
from utils.NutrientAPICalls import NutrientAPI
from utils.ConfigHandler import load_config


def prepareData():

    api_key = config('FDC_API_KEY')
    configs = load_config('./config.yaml')

    nutrient_api = NutrientAPI(api_key=api_key, configs=configs)

    # Test function
    nutrients = nutrient_api.getNutrient("butter")
