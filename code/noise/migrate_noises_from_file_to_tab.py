"""
Migrate noise 
from 
    noisy-queries-translation-pt.txt and noisy-queries-typo.txt
to 
    tab_noisy_query.csv
"""
import util_bd_dataframe  as util_bd_pandas

df_original_query,_ = util_bd_pandas.read_df_original_query_and_dict_val_idg()


# migrating noisy-queries-translation-pt
noisy_text_list = {'cod_original_query': [], 'text': []}
for line in open('data/noisy-queries-translation-pt.txt'):
    fields = line.strip().split()
    cod_query = fields[0]
    text_query = ' '.join(fields[1:])
    noisy_text_list['cod_original_query'].append(cod_query)
    noisy_text_list['text'].append(text_query)

util_bd_pandas.save_noisy_query(noisy_text_list,7, "Back translation (with portuguese)")

# migrating noisy-queries-typo-pt
noisy_text_list = {'cod_original_query': [], 'text': []}
for line in open('data/noisy-queries-typo.txt'):
    fields = line.strip().split()
    cod_query = fields[0]
    text_query = ' '.join(fields[1:])
    noisy_text_list['cod_original_query'].append(cod_query)
    noisy_text_list['text'].append(text_query)

util_bd_pandas.save_noisy_query(noisy_text_list,8, "With one typographical error")
