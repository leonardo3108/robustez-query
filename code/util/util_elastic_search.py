""" 
Utility functions related to elastic seach database
"""
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore

def return_doc_store():
    doc_store = ElasticsearchDocumentStore(
        host='localhost',
        username='', password='',
        index='robustez-query',
        similarity='dot_product'
    )
    print(f"\nQtd de documentos {doc_store.get_document_count()}")
    print(f"\nQtd de embeddings {doc_store.get_embedding_count()}")
    #print(f"\nDocumento.id=1020327: {doc_store.get_document_by_id('1020327')}")
    return doc_store