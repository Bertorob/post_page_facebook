import json

def read_config():
    with open('etc/config.json', 'r') as f:
        config = json.load(f)
    
    return config 
