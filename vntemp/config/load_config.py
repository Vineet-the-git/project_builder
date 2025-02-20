import yaml

def get_configs(config_path = 'config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config
