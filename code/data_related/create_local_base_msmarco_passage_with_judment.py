"""
Objetivo: criar base local msmarco-passage com julgamentos
"""

import requests
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore

#print(f"\nConfiguração do serviço ES: {requests.get('http://localhost:9200').json()}")
print(f"\nSituação do serviço ES: {requests.get('http://localhost:9200/_cluster/health').json()}")



passages = []

for passage in open('data/passages-with-judment.txt', encoding="utf8"):
    fields = passage.strip().split()
    passages.append((fields[0], ' '.join(fields[1:])))

print(f"\nPassage[0] com julgamento: {passages[0][0], passages[0][1]}")

data_carga_json = [
    {
        'content': passage[1],
        'id': passage[0],
        'meta': {
            'source': 'msmarco-passage-with-judment'
        }
    } for passage in passages
]

print(f"\nlen(data_carga_json) {len(data_carga_json)}")
print(f"Data_carga_json[0] {data_carga_json[0]}")

doc_store = ElasticsearchDocumentStore(
    host='localhost',
    username='', password='',
    index='robustez-query',
    similarity='dot_product'
)
doc_store.write_documents(data_carga_json)
