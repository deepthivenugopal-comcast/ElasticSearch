from modules.elasticsearch_client import get_es_client
from modules.data_retrieval import get_query_template, retrieve_data
from modules.csv_writer import write_to_csv


def main():
    es_client, index = get_es_client('config/config.json')
    query_template = get_query_template('config/queries.json', 'request1')
    data = retrieve_data(es_client, index, query_template)
    write_to_csv(data, 'output/data.csv')


if __name__ == "__main__":
    main()
