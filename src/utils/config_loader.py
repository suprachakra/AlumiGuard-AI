import yaml

def load_config(path='config/params.yaml'):
    """
    Loads configuration from a YAML file.
    """
    with open(path, 'r') as f:
        return yaml.safe_load(f)
