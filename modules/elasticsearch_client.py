from elasticsearch import Elasticsearch
import json
import os



def get_es_client(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The configuration file was not found: {config_path}")
    with open(config_path) as config_file:
        config = json.load(config_file)

    es = Elasticsearch(
        hosts=config['elasticsearch']['hosts'],
        http_auth=tuple(config['elasticsearch']['http_auth'])
    )
    return es, config['elasticsearch'].get('index','default_index')



config_path = 'config/config.json'
es_client, es_index = get_es_client(config_path)
print(f"Elasticsearch index: {es_index}")



