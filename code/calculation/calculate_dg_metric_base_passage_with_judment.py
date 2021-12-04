import time
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from util import util_bd_dataframe  as util_bd_pandas
const_epsilon = 10e-6

def calcular_desconto_ganho(base, value):
    # print(f"ndcg base: {base} ndcg value: {value}")
    return (value + const_epsilon) / (base + const_epsilon) - 1

# calcular para os tipos de ruídos nos contextos existentes

df_calculated_metric = util_bd_pandas.read_df_calculated_metric()
# util_bd_pandas.imprime_resumo_df(df_calculated_metric)

"""
Dropar existing records 
print(f"Records df_calculated_metric: {df_calculated_metric.shape[0]}")

print(f"Records with dg: {df_calculated_metric[df_calculated_metric['cod_metric'] == util_bd_pandas.const_cod_metric_dg_ndcg10].shape[0]}")

df_calculated_metric.drop(df_calculated_metric[df_calculated_metric['cod_metric'] == util_bd_pandas.const_cod_metric_dg_ndcg10].index, inplace=True)

print(f"After drop: records with dg: {df_calculated_metric[df_calculated_metric['cod_metric'] == util_bd_pandas.const_cod_metric_dg_ndcg10].shape[0]}")
print(f"Records df_calculated_metric: {df_calculated_metric.shape[0]}")

df_calculated_metric[['date_time_execution','cod_metric','cod_original_query','cod_noise_kind','cod_search_context','value','qtd_judment_assumed_zero_relevance','language']].to_csv('data/tab_calculated_metric.csv', sep = ',', index=False)   
"""

nDCG10_original = df_calculated_metric.query('cod_metric == "nDCG@10" and cod_noise_kind == 0').set_index(['cod_original_query', 'language', 'cod_search_context'])[['value']].to_dict()['value']
print(f"len(nDCG10_original): {len(nDCG10_original)} list(nDCG10_original.items())[:5]: {list(nDCG10_original.items())[:5]} list(nDCG10_original.items())[-5:]: {list(nDCG10_original.items())[-5:]}")

# teste    
# print(calcular_desconto_ganho(1030303, 4, 0.676534))

df_dg = df_calculated_metric.query('cod_metric == "nDCG@10"')[['cod_original_query','cod_noise_kind','cod_search_context','value','qtd_judment_assumed_zero_relevance','language']]
df_dg['value'] = df_dg.apply(lambda row:calcular_desconto_ganho(nDCG10_original[(row.cod_original_query, row.language, row.cod_search_context)], row.value), axis = 1)
util_bd_pandas.imprime_resumo_df(df_dg)

util_bd_pandas.save_dg_metric(df_dg)    

"""
# gravar valor zero para queries originais nos contextos existentes
df_noise_kind = util_bd_pandas.read_df_noise_kind()
df_search_context = util_bd_pandas.read_df_search_context()
df_original_metric,_ = util_bd_pandas.read_df_original_query_and_dict_val_idg()
df_dg = df_original_metric
del df_dg['val_idcg10']
del df_dg['text']
df_dg['cod_noise_kind'] = 0 
df_dg['value'] = 0 
df_dg =  df_dg.rename(columns={"cod": "cod_original_query"})
df_dg['qtd_judment_assumed_zero_relevance'] = 0
util_bd_pandas.imprime_resumo_df(df_dg)
for search_context in df_search_context['cod'].unique():
    df_dg['cod_search_context'] = search_context
    util_bd_pandas.save_dg_metric(df_dg)    
    del df_dg['date_time_execution']
    del df_dg['cod_metric']
util_bd_pandas.imprime_resumo_df(df_dg)

# gravar valor zero para queries originais em português nos contextos de portugues
df_noise_kind = util_bd_pandas.read_df_noise_kind()
df_search_context = util_bd_pandas.read_df_search_context_given_trec20_judment_pt()
df_original_metric,_ = util_bd_pandas.read_df_original_query_and_dict_val_idg()
df_dg = df_original_metric[df_original_metric['language']=='pt']
del df_dg['val_idcg10']
del df_dg['text']
df_dg['cod_noise_kind'] = 0 
df_dg['value'] = 0 
df_dg = df_dg.rename(columns={"cod": "cod_original_query"})
df_dg['qtd_judment_assumed_zero_relevance'] = 0
util_bd_pandas.imprime_resumo_df(df_dg)
for search_context in df_search_context['cod'].unique():
    df_dg['cod_search_context'] = search_context
    util_bd_pandas.save_dg_metric(df_dg)    
    del df_dg['date_time_execution']
    del df_dg['cod_metric']
util_bd_pandas.imprime_resumo_df(df_dg)


"""


