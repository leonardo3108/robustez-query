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
# from util import util_elastic_search as util_es
df=util_bd_pandas.read_df_search_context_given_trec20_judment_pt()
# df = df[(df['cod_noise_kind']==0) & (df['language']=='pt')]
util_bd_pandas.imprime_resumo_df(df)

