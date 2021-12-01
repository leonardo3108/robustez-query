import time
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from util import util_bd_dataframe  as util_bd_pandas

def calcular_desconto_ganho(base, value):
    # print(f"ndcg base: {base} ndcg value: {value}")
    if base:
        return value / base - 1
    return float("NaN")

# gravar valor zero para queries originais nos contextos existentes
df_noise_kind = util_bd_pandas.read_df_noise_kind()
df_search_context = util_bd_pandas.read_df_search_context()
df_original_metric,_ = util_bd_pandas.read_df_original_query()
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


# calcular para os tipos de ruídos nos contextos existentes

df_calculated_metric = util_bd_pandas.read_df_calculated_metric()
# util_bd_pandas.imprime_resumo_df(df_calculated_metric)

nDCG10_original = df_calculated_metric.query('cod_metric == "nDCG@10" and cod_noise_kind == 0').set_index(['cod_original_query', 'language', 'cod_search_context'])[['value']].to_dict()['value']
print(list(nDCG10_original.items())[:10])

# teste    
# print(calcular_desconto_ganho(1030303, 4, 0.676534))

df_dg = df_calculated_metric.query('cod_metric == "nDCG@10" and cod_noise_kind != 0')[['cod_original_query','cod_noise_kind','cod_search_context','value','qtd_judment_assumed_zero_relevance','language' ]]
df_dg['value'] = df_dg.apply(lambda row:calcular_desconto_ganho(nDCG10_original[(row.cod_original_query, row.cod_search_context, row.language)], row.value), axis = 1)
# util_bd_pandas.imprime_resumo_df(df_dg)

util_bd_pandas.save_dg_metric(df_dg)    


