import requests
import math
import util_bd_dataframe  as util_bd_pandas
import util 
import util_elastic_search as util_es
from haystack.retriever.dense import DensePassageRetriever


df_noisy_query = util_bd_pandas.read_df_noisy_query()
df_original_query, dict_val_idcg10 = util_bd_pandas.read_df_original_query()
df_noisy_query = util_bd_pandas.read_df_noisy_query()
dict_judment, dict_scale_relevance = util.load_judment()

doc_store = util_es.return_doc_store()
retriever = DensePassageRetriever(
    document_store=doc_store,
    query_embedding_model='facebook/dpr-question_encoder-single-nq-base',
    passage_embedding_model='facebook/dpr-ctx_encoder-single-nq-base',
    # use_gpu=True, 
    use_gpu=False,
    embed_title=True
)




# Calculate dcg10 and ndcg10 of noisy queries


for noise_kind in df_noisy_query['cod_noise_kind'].unique():
  calculated_metric = {'cod_original_query':[],'dcg10':[],'ndcg10':[]}
  for index, row in df_noisy_query[df_noisy_query['cod_noise_kind']==noise_kind].iterrows():
    cod_original_query = row["cod_original_query"]
    idcg10 = dict_val_idcg10[cod_original_query]
    query_text = row["text"]
    # calculating dcg10 for query
    dcg10 = 0
    for i, result_busca in enumerate(retriever.retrieve(query_text, top_k=10)):
      if i >= 10:
        raise 'Error: more than 10 retrieved!'
      docid = result_busca.id
      # print(f'docid retrieved {docid}')
      if (cod_original_query, docid) not in dict_judment:
        print(f'Query and passage_id not in judment:{(cod_original_query, docid)}. Assumed zero relevance. ')
      eval = dict_judment.get((cod_original_query, docid), 0)
      dcg10 += (2**int(eval)-1) / math.log2(i+2)
    # calculate ndcg10 for query
    ndcg10 = dcg10 / idcg10
    # print(f"query {cod_original_query} has dcg10 {dcg10} ndcg10 {ndcg10} for idcg10 {idcg10} ")
    calculated_metric['cod_original_query'].append(cod_original_query)
    calculated_metric['dcg10'].append(dcg10)
    calculated_metric['ndcg10'].append(ndcg10)
  util_bd_pandas.save_calculated_metric(calculated_metric, cod_search_context=util_bd_pandas.const_cod_search_context_dpr, cod_noise_kind=noise_kind)    

