"""
just to explore coding
"""

import pandas as pd
import numpy as np
import util_bd_dataframe  as util_bd_pandas
import time

print("oi")
df = util_bd_pandas.read_df_search_context()
util_bd_pandas.imprime_resumo_df(df)
print(4 in df['cod'])
print(df['cod'])
print(list(df['cod']))
print(4 in list(df['cod']))