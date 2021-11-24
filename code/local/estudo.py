"""
just to explore coding
"""
print('oi')

import pandas as pd
import numpy as np
import util_bd_dataframe  as util_bd_pandas
import time

pd.set_option("display.max_columns", None)  # "display.max_rows", None,
print("oi")
df = util_bd_pandas.read_df_noise_kind()
util_bd_pandas.imprime_resumo_df(df)