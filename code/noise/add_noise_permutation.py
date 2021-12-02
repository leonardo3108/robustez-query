"""
Gera queries com ruído
Lógica
    Ler original query
    Aplicar ruído
    Salvar noisy query

"""

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
from util import util_bd_dataframe  as util_bd_pandas
import util_noise_functions as util_noise

language_context = 'pt'

df_original_query,_ = util_bd_pandas.read_df_original_query_and_dict_val_idg()
df_original_query = df_original_query[df_original_query['language']==language_context]
util_bd_pandas.imprime_resumo_df(df_original_query)

# Trocando primeira com segunda
noisy_text_list = {'cod_original_query': [], 'text': []}
for index, original_query in df_original_query.iterrows():
    noisy_text = util_noise.token_permutation_list_index_pair(original_query['text'],[(0,1)])
    noisy_text_list['cod_original_query'].append(original_query['cod'])
    noisy_text_list['text'].append(noisy_text)
util_bd_pandas.save_noisy_query(noisy_text_list,1,language_context)


# Trocando penúltima com última
noisy_text_list = {'cod_original_query': [], 'text': []}
for index, original_query in df_original_query.iterrows():
    lista_tokens = util_noise.return_tokens(original_query['text'])
    noisy_text = util_noise.token_permutation_list_index_pair(original_query['text'],[(len(lista_tokens)-2,len(lista_tokens)-1)])
    noisy_text_list['cod_original_query'].append(original_query['cod'])
    noisy_text_list['text'].append(noisy_text)
util_bd_pandas.save_noisy_query(noisy_text_list,2,language_context)


# Trocando primeira e última
noisy_text_list = {'cod_original_query': [], 'text': []}
for index, original_query in df_original_query.iterrows():
    lista_tokens = util_noise.return_tokens(original_query['text'])
    noisy_text = util_noise.token_permutation_list_index_pair(original_query['text'],[(0,len(lista_tokens)-1)])
    noisy_text_list['cod_original_query'].append(original_query['cod'])
    noisy_text_list['text'].append(noisy_text)
util_bd_pandas.save_noisy_query(noisy_text_list,3,language_context)
