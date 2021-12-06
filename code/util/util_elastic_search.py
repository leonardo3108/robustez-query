""" 
Utility functions related to elastic seach database
"""
from tqdm import tqdm
import requests
import sys
from pathlib import Path
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
from haystack.retriever.dense import DensePassageRetriever
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from util import util_bd_dataframe as util_bd_pandas
from util import util_retriever as util_ret

const_index_name_portuguese_base = 'msmarco-passage-with-judment-in-portuguese'
const_index_name_english_base ='robustez-query'



def show_all_indexes():
    return_text = requests.get('http://localhost:9200/_cat/indices?v').content.decode('unicode_escape')
    print(f"\nElastic Search indexes: {return_text}")
    print(f"\n Situation of portuguese index: {requests.get('http://localhost:9200/'+const_index_name_portuguese_base).json()}")
    print(f"\n Situation of english index: {requests.get('http://localhost:9200/'+const_index_name_english_base).json()}")
    print(f"\n Doctos of portuguese index: {requests.get('http://localhost:9200/'+const_index_name_portuguese_base+'/_search?pretty=true').content.decode('unicode_escape')}")    
def return_doc_store(parm_language:str):
    assert parm_language in ['en','pt'], f"parm_language: {parm_language} is not valid: in ['en','pt']"

    if parm_language == 'en':
        index_name =const_index_name_english_base
    elif parm_language == 'pt':
        index_name =const_index_name_portuguese_base

    doc_store = ElasticsearchDocumentStore(
        host='localhost',
        username='', password='',
        index=index_name,
        create_index= False,
        similarity='dot_product'
    )
    print(f"\nQtd de documentos {doc_store.get_document_count()}")
    print(f"\nQtd de embeddings {doc_store.get_embedding_count()}")
    print(f"\nDocumento.id=1020327: {doc_store.get_document_by_id('1020327')}")
    return doc_store

def update_embeddings(parm_language:str):
    assert parm_language in ['en','pt'], f"parm_language: {parm_language} is not valid: in ['en','pt']"

    #print(f"\nConfiguração do serviço ES: {requests.get('http://localhost:9200').json()}")
    print(f"\nSituação do serviço ES: {requests.get('http://localhost:9200/_cluster/health').json()}")

    doc_store = return_doc_store(parm_language)
    retriever = util_ret.init_retriever_es_dpr(doc_store, parm_language)
    doc_store.update_embeddings(retriever=retriever)


def create_doc_store(parm_language:str):
    assert parm_language in ['en','pt'], f"parm_language: {parm_language} is not valid: in ['en','pt']"
    #print(f"\nConfiguração do serviço ES: {requests.get('http://localhost:9200').json()}")
    print(f"\nSituação do serviço ES: {requests.get('http://localhost:9200/_cluster/health').json()}")
    df_passage = util_bd_pandas.read_df_passage_with_judment()
    data_carga_json = []
    for index, passage in tqdm(df_passage[df_passage['language']==parm_language].iterrows(), 'progress-bar'):
        data_carga_json.append({'content': passage['text'],'id': passage['cod_docto'], 'meta': {'source': 'msmarco-passage-with-judment-in-portuguese'}})
    # print(f"\nPassage[0] com julgamento: {passages[0][0], passages[0][1]}")

    print(f"\nlen(data_carga_json) {len(data_carga_json)}")
    print(f"Data_carga_json[0] {data_carga_json[0]}")
    # print(f"Data_carga_json {data_carga_json}")

    if parm_language == 'en':
        index_name =const_index_name_english_base
    elif parm_language == 'pt':
        index_name =const_index_name_portuguese_base

    doc_store = ElasticsearchDocumentStore(
        host='localhost',
        username='', password='',
        index=index_name,
        similarity='dot_product'
    )
    print(f"\nbefore write")

    print(f"\nQtd de documentos {doc_store.get_document_count()}")
    print(f"\nQtd de embeddings {doc_store.get_embedding_count()}")
    print(f"\nDocumento.id=1020327: {doc_store.get_document_by_id('1020327')}")

    doc_store.write_documents(data_carga_json)

    print(f"\nafter write")

    print(f"\nQtd de documentos {doc_store.get_document_count()}")
    print(f"\nQtd de embeddings {doc_store.get_embedding_count()}")
    print(f"\nDocumento.id=1020327: {doc_store.get_document_by_id('1020327')}")