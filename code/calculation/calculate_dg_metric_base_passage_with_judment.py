import time
import util_bd_dataframe  as util_bd_pandas

def calcular_desconto_ganho(base, value):
    # print(f"ndcg base: {base} ndcg value: {value}")
    if base:
        return value / base - 1
    return float("NaN")


df_calculated_metric = util_bd_pandas.read_df_calculated_metric()
# util_bd_pandas.imprime_resumo_df(df_calculated_metric)

nDCG10_original = df_calculated_metric.query('cod_metric == "nDCG@10" and cod_noise_kind == 0').set_index(['cod_original_query', 'cod_search_context'])[['value']].to_dict()['value']
print(list(nDCG10_original.items())[:10])

# teste    
# print(calcular_desconto_ganho(1030303, 4, 0.676534))

df_dg = df_calculated_metric.query('cod_metric == "nDCG@10" and cod_noise_kind != 0')[['cod_original_query','cod_noise_kind','cod_search_context','value','qtd_judment_assumed_zero_relevance' ]]
df_dg['value'] = df_dg.apply(lambda row:calcular_desconto_ganho(nDCG10_original[(row.cod_original_query, row.cod_search_context)], row.value), axis = 1)
# util_bd_pandas.imprime_resumo_df(df_dg)

util_bd_pandas.save_dg_metric(df_dg)    

exit()
df_dg.dropna(inplace=True)
df_dg