from elasticsearch import Elasticsearch

class ElasticSearchConnection:

    def __init__(self):
        pass

    def get_connection(self):
        elasticSearchConnection = Elasticsearch()
        return elasticSearchConnection

