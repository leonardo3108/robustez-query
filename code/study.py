"""
just to explore coding
"""
print('oi')
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath('.'))
    sys.path.append(os.path.abspath('.\.'))
import pandas as pd
from util import util_bd_dataframe as util_bd_pandas

df_calculated_metric =  util_bd_pandas.read_df_calculated_metric()

df_noisy_query = read_df_noisy_query()
df = pd.merge(df_calculated_metric, df_noisy_query, left_on=['cod_original_query', 'language', 'cod_noise_kind'], right_on=['cod_original_query', 'language', 'cod_noise_kind'],suffixes=(None,'_noise_kind'))
df['qtd_tokens'] = df.apply(lambda row:count_tokens(row.cod_original_query, row.language, row.cod_search_context)], row.value), axis = 1)
util_bd_pandas.imprime_resumo_df(df)

exit()

# assert not exists calculated metric
for index, row in df_calculated_metric[df_calculated_metric['cod_noise_kind'] ==0].iterrows():           
    condition = f"cod_original_query == {row['cod_original_query']} &  cod_noise_kind == {row['cod_noise_kind']} & cod_search_context == {row['cod_search_context']} & cod_metric == 'DG:nDCG@10' & language == '{row['language']}'"
    assert df_calculated_metric.query(condition).shape[0] ==1, f"Can not save again calculus already done for condition {condition}"

# from util import util_elastic_search as util_es
df=util_bd_pandas.read_df_search_context_given_trec20_judment_pt()
# df = df[(df['cod_noise_kind']==0) & (df['language']=='pt')]

