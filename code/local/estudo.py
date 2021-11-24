"""
just to explore coding
"""
print('oi')

import pandas as pd
import numpy as np
import util_bd_dataframe  as util_bd_pandas
import time

print("oi")
df = util_bd_pandas.read_df_calculated_metric_with_label()
util_bd_pandas.imprime_resumo_df(df)