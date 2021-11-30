"""
just to explore coding
"""

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.abspath('.'))
    sys.path.append(os.path.abspath('.\.'))
print('oi')

import pandas as pd
import numpy as np
from util import util_bd_dataframe as util_bd_pandas

pd.set_option("display.max_columns", None)  # "display.max_rows", None,
print("oi")
df = util_bd_pandas.read_df_search_context()
util_bd_pandas.imprime_resumo_df(df)
#util_bd_pandas.imprime_resumo_df(df[df['abbreviation_ranking_function']!='BM25'])