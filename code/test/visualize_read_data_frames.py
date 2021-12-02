"""
just to explore coding
"""
print('oi')
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath('.'))
    sys.path.append(os.path.abspath('..'))

import pandas as pd
from util import util_bd_dataframe as util_bd_pandas

pd.set_option("display.max_columns", None)  # "display.max_rows", None,



df = util_bd_pandas.read_df_noise_kind()
util_bd_pandas.imprime_resumo_df(df)

exit()
df, dictaux = util_bd_pandas.read_df_original_query_and_dict_val_idg()
util_bd_pandas.imprime_resumo_df(df)
print(dictaux)

df = util_bd_pandas.read_df_search_context()
util_bd_pandas.imprime_resumo_df(df)

df = util_bd_pandas.read_df_calculated_metric()
util_bd_pandas.imprime_resumo_df(df)


df = util_bd_pandas.read_df_calculated_metric_with_label()
util_bd_pandas.imprime_resumo_df(df)
