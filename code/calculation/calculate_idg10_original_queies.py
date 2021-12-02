"""
Calculate idg on base passage with judment
"""

import sys
import math
import pandas as pd
import numpy as np
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
from util import util_bd_dataframe as util_bd_pandas

df_judment, dict_val_relevance = util_bd_pandas.read_df_judment_and_dict_relevance()
util_bd_pandas.imprime_resumo_df(df_judment)
# print(dict_val_relevance)


query_with_judment = {}
for i, (cod_query, cod_docto) in enumerate(dict_val_relevance.keys()):
    if cod_query not in query_with_judment:
        query_with_judment[cod_query] = []
    query_with_judment[cod_query].append(int(dict_val_relevance[(cod_query, cod_docto)]))

print(f"len(query_with_judment) = {len(query_with_judment)}")
print(f"query_with_judment[23849] = {query_with_judment[23849]}")


best10relevances = {}
print('Best 10 judgings per query:')
for cod_query in query_with_judment.keys():
    best10relevances[cod_query] = sorted(query_with_judment[cod_query], reverse = True)[:10]
    # print('{}: {}'.format(query, best10relevances[query]))
print(f"best10relevances[23849] = {best10relevances[23849]}")

idcg = {}
print('IDCG calculation per query:')
for cod_query in best10relevances.keys():
    acumulated_idcg = 0
    for i, judging in enumerate(best10relevances[cod_query]):
        acumulated_idcg += (2**int(judging)-1) / math.log2(i+2)  
    idcg[cod_query] = acumulated_idcg   

print(f"idcg[23849] = {idcg[23849]}")

df_original_query = pd.read_csv('data/tab_original_query.csv', sep = ';', 
    header=0, dtype= {'cod':np.int64, 'language':str, 'text':str, 'val_idcg10': str})
df_original_query['val_idcg10'] = df_original_query['val_idcg10'].astype(float)   

for index, row in df_original_query.iterrows():
    df_original_query.loc[index, 'val_idcg10'] = idcg[row['cod']]
util_bd_pandas.imprime_resumo_df(df_original_query)

df_original_query[['cod', 'language', 'text', 'val_idcg10']].to_csv('data/tab_original_query.csv', sep = ';', index=False)   

