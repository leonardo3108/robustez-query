"""
just to investigate score returned by rerank in searches
"""
print('oi')
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath('.'))
    sys.path.append(os.path.abspath('.')+'\code')
    sys.path.append(os.path.abspath('.\.'))
import pandas as pd
from util import util_bd_dataframe as util_bd_pandas
pd.set_option("display.max_columns", None)  # "display.max_rows", None

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

parm_type_retrieval = 'rerank'
parm_language = 'pt'

_, dict_val_idcg10 = util_bd_pandas.read_df_original_query_and_dict_val_idg()
df_noisy_query = util_bd_pandas.read_df_noisy_query()
_, dict_judment = util_bd_pandas.read_df_judment_and_dict_relevance()

doc_store = util_es.return_doc_store(parm_language)
retriever = util_ret.init_retriever_es_bm25(doc_store)
if parm_language == 'en':
    reranker = MonoT5(pretrained_model_name_or_path='castorini/monot5-base-msmarco') # default: 'castorini/monot5-base-msmarco'        
    search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_en
else:  
    #search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_model_mono_ptt5_unicamp_base_pt_msmarco_100k
    #reranker = MonoT5(pretrained_model_name_or_path='unicamp-dl/ptt5-base-pt-msmarco-100k', token_false= '▁não', token_true='▁sim')       
    #id_modelo = 'ptt5-base-msmarco-100k' 


    # search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_model_multi_pt_msmarco
    reranker = MonoT5(pretrained_model_name_or_path='unicamp-dl/mt5-base-multi-msmarco')     
    id_modelo = 'mt5-base-multi-msmarco'    


    # try out unicamp-dl/mt5-base-en-pt-msmarco  
    # results expected worse: https://arxiv.org/pdf/2108.13897

    # search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_model_en_pt_msmarco
    # reranker = MonoT5(pretrained_model_name_or_path='unicamp-dl/mt5-base-en-pt-msmarco')        


    # search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_model_small_pt
    # reranker = MonoT5(pretrained_model_name_or_path='unicamp-dl/ptt5-small-portuguese-vocab', token_false= '▁não', token_true='▁sim')        

    # search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_model_base_pt
    # reranker = MonoT5(pretrained_model_name_or_path='unicamp-dl/ptt5-base-portuguese-vocab', token_false= '▁não', token_true='▁sim')        

    # search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_model_base_pt_dif_token
    # reranker = MonoT5(pretrained_model_name_or_path='unicamp-dl/ptt5-base-portuguese-vocab', token_false= '▁false', token_true='▁true')        


    # search_context = util_bd_pandas.const_cod_search_context_rerank_trec20_judment_model_mono_ptt5_unicamp_base_t5_vocab
    # reranker = MonoT5(pretrained_model_name_or_path='unicamp-dl/ptt5-base-t5-vocab', token_false= '▁false', token_true='▁true')        


# Calculate dcg10 and ndcg10 of noisy queries
bm25_qtd = 50
rerank_qtd = 20
calculated_score = {'id_modelo':[], 'bm25_qtd': [], 'rerank_qtd':[], 'cod_original_query':[],'score':[],'eval':[], 'qtd_judment_assumed_zero_relevance':[],'noise_kind':[]}
for noise_kind in tqdm(df_noisy_query[df_noisy_query['language']==parm_language]['cod_noise_kind'].unique(), "Progress bar - Noise kind"):
    for index, row in tqdm(df_noisy_query[(df_noisy_query['cod_noise_kind']==noise_kind) & (df_noisy_query['language']==parm_language)].iterrows(), "Progress bar - query"):       
        cod_original_query = row["cod_original_query"]
        query_text = row["text"]
        doctos_returned_bm25 = retriever.retrieve(query_text, top_k=bm25_qtd)
        list_doctos = []
        for docto in doctos_returned_bm25:
            dt = class_docto_encontrado(id=docto.id, text=docto.content)
            list_doctos.append(dt)
        query_busca = Query(query_text)
        list_docs = reranker.rerank(query_busca, list_doctos)[:20]

        # calculating dcg10 for query
        dcg10 = 0
        qtd_judment_assumed_zero_relevance = 0
        for i, docto_encontrado in enumerate(list_docs):
            docid = docto_encontrado.id
            if (cod_original_query, docid) not in dict_judment:
                calculated_score['qtd_judment_assumed_zero_relevance'].append(1)
                qtd_judment_assumed_zero_relevance += 1
            else:
                calculated_score['qtd_judment_assumed_zero_relevance'].append(0)
            eval = dict_judment.get((cod_original_query, docid), 0)
            calculated_score['id_modelo'].append(id_modelo)
            calculated_score['bm25_qtd'].append(bm25_qtd)
            calculated_score['rerank_qtd'].append(rerank_qtd)            
            calculated_score['cod_original_query'].append(cod_original_query)
            calculated_score['noise_kind'].append(noise_kind)
            calculated_score['score'].append(docto_encontrado.score)
            calculated_score['eval'].append(eval)
        # print(f"+ cod_original_query: {cod_original_query} \nScore: {calculated_score['score']} \nEval: {calculated_score['eval']}")
        # calculate ndcg10 for query
        print(f" Done for noise_kind: {noise_kind} em {time.strftime('%Y-%m-%d %H:%M:%S')}")    
    temp_df = pd.DataFrame.from_dict(calculated_score)  
    temp_df.to_csv('data/comparative_rerank_score_judment_eval_mt5.csv', sep = ';', index=False)   
    # break

