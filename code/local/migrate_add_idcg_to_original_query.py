"""
Migrate noise 
from 
    noisy-queries-translation-pt.txt and noisy-queries-typo.txt
to 
    tab_noisy_query.csv
"""
import util_bd_dataframe  as util_bd_pandas

df_original_query,_ = util_bd_pandas.read_df_original_query()


# migrating noisy-queries-translation-pt
idcg={}
noisy_text_list = {'cod_original_query': [], 'text': []}
for pos, line in enumerate(open('data/idcg.csv')):
    if pos == 0:
        continue
    fields = line.strip().split(',')
    cod_query = int(fields[0])
    idcg[cod_query] = float(fields[1].strip())
print(idcg)

for i, row in df_original_query.iterrows():
    cod_original_query = row['cod']
    val_idcg_original_query = idcg[cod_original_query]
    df_original_query.at[i,'val_idcg10'] = val_idcg_original_query

print(df_original_query.head(4))

util_bd_pandas.save_df_original_query(df_original_query)
