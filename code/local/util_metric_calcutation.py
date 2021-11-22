""" 
Utility functions for calculatint Informational Retrieval Metrics
"""
import math
import util_elastic_search as util_es
import util_retriever as util_ret
import util_bd_dataframe as util_bd_pandas

def calculate_metric_in_es(parm_type_retrieval:str):
    """ Calcuate metrics in base of elastic search 
        Considers search mechanism specified in parm_type_retrieval

    Args:
        parm_type_retrieval (str): dpr x bm25

    """
    assert parm_type_retrieval in ("dpr","bm25"), f"parm_type_retrieval: {parm_type_retrieval} expected to be in ('dpr','bm25')"


    _, dict_val_idcg10 = util_bd_pandas.read_df_original_query()
    df_noisy_query = util_bd_pandas.read_df_noisy_query()
    dict_judment, _ = util_bd_pandas.load_judment()

    doc_store = util_es.return_doc_store()
    if parm_type_retrieval == 'bm25':
        retriever = util_ret.init_retriever_es_bm25(doc_store)
        search_context = util_bd_pandas.const_cod_search_context_bm25_trec20_judment        
    else:
        retriever = util_ret.init_retriever_es_dpr(doc_store)
        search_context = util_bd_pandas.const_cod_search_context_dpr_trec20_judment        

    # Calculate dcg10 and ndcg10 of noisy queries
    for noise_kind in df_noisy_query['cod_noise_kind'].unique():
        calculated_metric = {'cod_original_query':[],'dcg10':[],'ndcg10':[], 'qtd_judment_assumed_zero_relevance':[]}
        for index, row in df_noisy_query[df_noisy_query['cod_noise_kind']==noise_kind].iterrows():
            cod_original_query = row["cod_original_query"]
            idcg10 = dict_val_idcg10[cod_original_query]
            query_text = row["text"]


            # calculating dcg10 for query
            dcg10 = 0
            qtd_judment_assumed_zero_relevance = 0
            for i, result_busca in enumerate(retriever.retrieve(query_text, top_k=10)):
                if i >= 10:
                    raise 'Error: more than 10 retrieved!'
                docid = result_busca.id
                # print(f'docid retrieved {docid}')
                if (cod_original_query, docid) not in dict_judment:
                    print(f'Query and passage_id not in judment:{(cod_original_query, docid)}. Assumed zero relevance. ')
                    qtd_judment_assumed_zero_relevance += 1
                eval = dict_judment.get((cod_original_query, docid), 0)
                dcg10 += (2**int(eval)-1) / math.log2(i+2)
                # calculate ndcg10 for query
            ndcg10 = dcg10 / idcg10
            # print(f"query {cod_original_query} has dcg10 {dcg10} ndcg10 {ndcg10} for idcg10 {idcg10} ")


            calculated_metric['cod_original_query'].append(cod_original_query)
            calculated_metric['dcg10'].append(dcg10)
            calculated_metric['ndcg10'].append(ndcg10)
            calculated_metric['qtd_judment_assumed_zero_relevance'].append(qtd_judment_assumed_zero_relevance)
        util_bd_pandas.save_calculated_metric(calculated_metric, cod_search_context=search_context, cod_noise_kind=noise_kind)    

