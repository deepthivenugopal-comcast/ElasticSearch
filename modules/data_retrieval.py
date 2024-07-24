import json
import os
from elasticsearch import Elasticsearch


def get_es_client(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The configuration file was not found: {config_path}")
    with open(config_path) as config_file:
        config = json.load(config_file)

    es = Elasticsearch(
        hosts=config['elasticsearch']['hosts'],
        http_auth=tuple(config['elasticsearch']['http_auth'])
    )
    return es, config['elasticsearch']['index']

def get_query_template(query_path, template_name):
    with open(query_path) as query_file:
        queries = json.load(query_file)
    if template_name not in queries:
        raise KeyError(f"The template name '{template_name}' was not found in the queries.")
    return queries[template_name]

def retrieve_data(es_client, index, query):
    response = es_client.search(index=index, body=query)
    return [hit['_source'] for hit in response['hits']['hits']]


config_path = 'config/config.json'
es_client, es_index = get_es_client(config_path)

query_path = 'config/queries.json'  # Update the path to your actual queries.json file
template_name = 'request1'

try:
    query_template = get_query_template(query_path, template_name)
    print("Query template:", query_template)

    results = retrieve_data(es_client, es_index, query_template)
    print("Retrieved data:", results)

except KeyError as e:
    print(e)
except Exception as e:
    print("An error occurred:", e)

