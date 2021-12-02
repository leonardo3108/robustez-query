""" 
Utility functions for calculatint Informational Retrieval Metrics
"""
import math
import time
import sys
from tqdm import tqdm
from pathlib import Path
from pygaggle.rerank.base import Query
from pygaggle.rerank.base import hits_to_texts
from pygaggle.rerank.transformer import MonoT5 
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
from util import util_elastic_search as util_es
from util import util_retriever as util_ret
from util import util_bd_dataframe as util_bd_pandas

class class_docto_encontrado(object):

    def __init__(self, id, text:str):
        self._id = id
        self._text = text

    @property
    def text(self):
        return self._text
    @property
    def id(self):
        return self._id

def calculate_metric_in_es(parm_type_retrieval:str, parm_language:str):
    """ Calcuate metrics in base of elastic search 
        Considers search mechanism specified in parm_type_retrieval

    Args:
        parm_type_retrieval (str): dpr, bm25, rerank

    """
    assert parm_type_retrieval in ("dpr","bm25","rerank"), f"parm_type_retrieval: {parm_type_retrieval} expected to be in ('dpr','bm25')"
    assert parm_language in ['en','pt'], f"parm_language: {parm_language} is not valid: in ['en','pt']"

    _, dict_val_idcg10 = util_bd_pandas.read_df_original_query_and_dict_val_idg()
    df_noisy_query = util_bd_pandas.read_df_noisy_query()
    _, dict_judment = util_bd_pandas.read_df_judment_and_dict_relevance()

    doc_store = util_es.return_doc_store(parm_language)
    if parm_type_retrieval == 'bm25':
        retriever = util_ret.init_retriever_es_bm25(doc_store)
        if parm_language == 'en':
            search_context = util_bd_pandas.const_cod_search_context_bm25_trec20_judment_en        
        else:
            search_context = util_bd_pandas.const_cod_search_context_bm25_trec20_judment_pt        

    elif parm_type_retrieval == 'dpr':
        retriever = util_ret.init_retriever_es_dpr(doc_store, parm_language)
        if parm_language == 'en':
            search_context = util_bd_pandas.const_cod_search_context_dpr_trec20_judment_en     
        else:
            search_context = util_bd_pandas.const_cod_search_context_dpr_trec20_judment_pt  
    else:   
        reranker = MonoT5()        
        retriever = util_ret.init_retriever_es_bm25(doc_store, parm_language)
        if parm_language == 'en':
            search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_en
        else:
            search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_pt


    # Calculate dcg10 and ndcg10 of noisy queries
    for noise_kind in tqdm(df_noisy_query[df_noisy_query['language']==parm_language]['cod_noise_kind'].unique(), "Progress bar - Noise kind"):
        calculated_metric = {'cod_original_query':[],'dcg10':[],'ndcg10':[], 'qtd_judment_assumed_zero_relevance':[]}
        for index, row in tqdm(df_noisy_query[(df_noisy_query['cod_noise_kind']==noise_kind) & (df_noisy_query['language']==parm_language)].iterrows(), "Progress bar - query"):       
            cod_original_query = row["cod_original_query"]
            idcg10 = dict_val_idcg10[(cod_original_query, parm_language)]
            query_text = row["text"]

            # retrieve documents
            if parm_type_retrieval in ('bm25','dpr'):
                list_docs = retriever.retrieve(query_text, top_k=10)
            else: # 'rerank'
                doctos_returned_bm25 = retriever.retrieve(query_text, top_k=100)
                list_doctos = []
                for docto in doctos_returned_bm25:
                    dt = class_docto_encontrado(id=docto.id, text=docto.content)
                    list_doctos.append(dt)
                query_busca = Query(query_text)
                list_docs = reranker.rerank(query_busca, list_doctos)[:10]

            # calculating dcg10 for query
            dcg10 = 0
            qtd_judment_assumed_zero_relevance = 0
            for i, docto_encontrado in enumerate(list_docs):
                if i >= 10:
                    raise 'Error: more than 10 retrieved!'
                docid = docto_encontrado.id
                if (cod_original_query, docid) not in dict_judment:
                    # print(f'Query and passage_id not in judment:{(cod_original_query, docid)}. Assumed zero relevance. ')
                    qtd_judment_assumed_zero_relevance += 1
                eval = dict_judment.get((cod_original_query, docid), 0)
                dcg10 += (2**int(eval)-1) / math.log2(i+2)

            # calculate ndcg10 for query
            ndcg10 = dcg10 / idcg10

            # add values to lists
            calculated_metric['cod_original_query'].append(cod_original_query)
            calculated_metric['dcg10'].append(dcg10)
            calculated_metric['ndcg10'].append(ndcg10)
            calculated_metric['qtd_judment_assumed_zero_relevance'].append(qtd_judment_assumed_zero_relevance)
        util_bd_pandas.save_calculated_metric(calculated_metric, cod_search_context=search_context, cod_noise_kind=noise_kind,parm_language=parm_language)    
        print(f" Done for noise_kind: {noise_kind} em {time.strftime('%Y-%m-%d %H:%M:%S')}")        

