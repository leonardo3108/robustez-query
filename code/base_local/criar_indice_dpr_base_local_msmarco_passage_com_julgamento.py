"""
Objetivo: criar base local msmarco-passage com julgamentos
"""
import requests
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
from haystack.retriever.dense import DensePassageRetriever

#print(f"\nConfiguração do serviço ES: {requests.get('http://localhost:9200').json()}")
print(f"\nSituação do serviço ES: {requests.get('http://localhost:9200/_cluster/health').json()}")


doc_store = ElasticsearchDocumentStore(
    host='localhost',
    username='', password='',
    index='robustez-query',
    similarity='dot_product'
)

retriever = DensePassageRetriever(
    document_store=doc_store,
    query_embedding_model='facebook/dpr-question_encoder-single-nq-base',
    passage_embedding_model='facebook/dpr-ctx_encoder-single-nq-base',
    use_gpu=True,
    embed_title=True
)

doc_store.update_embeddings(retriever=retriever)