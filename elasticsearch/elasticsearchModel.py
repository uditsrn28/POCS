from elasticsearchconnection import ElasticSearctesthConnection

class ElasticSearchModel:
    def __init__(self):
        self.__elasticsearchClient = ElasticSearctesthConnection().get_connection()

    def insert_in_elasticsearch(self, index, type, id, body):
        res = self.__elasticsearchClient.index(index=index, doc_type=type, id=id, body=body)
        return res

    def get_in_elasticsearch(self, index, type, id):
        res = self.__elasticsearchClient.get(index=index, doc_type=type, id=id)
        return res

    def search_in_elasticsearch(self, index, search_body):
        res = self.__elasticsearchClient.search(index=index, body=search_body)
        return res

    def refresh_index_elasticsearch(self, index):
        res = self.__elasticsearchClient.indices.refresh(index=index)
        return res
