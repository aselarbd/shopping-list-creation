import yaml


# Configuration handler function
def load_config(config_file):
    with open(config_file, 'r', encoding="utf-8") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
