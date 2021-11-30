"""
Objetivo: criar base local msmarco-passage com julgamentos
"""
import requests
import util_elastic_search as util_es
from haystack.retriever.dense import DensePassageRetriever

#print(f"\nConfiguração do serviço ES: {requests.get('http://localhost:9200').json()}")
print(f"\nSituação do serviço ES: {requests.get('http://localhost:9200/_cluster/health').json()}")

doc_store = util_es.return_doc_store()

retriever = DensePassageRetriever(
    document_store=doc_store,
    query_embedding_model='facebook/dpr-question_encoder-single-nq-base',
    passage_embedding_model='facebook/dpr-ctx_encoder-single-nq-base',
    # use_gpu=True, 
    use_gpu=False,
    embed_title=True
)

print(f"\nÍndices do serviço ES: {requests.get('http://localhost:9200/_cat/indices')}")

doc_store.update_embeddings(retriever=retriever)

print(f"\nÍndices do serviço ES: {requests.get('http://localhost:9200/_cat/indices')}")
