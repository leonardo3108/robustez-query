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
from googletrans import Translator

translator = Translator()
abbreviation_portuguese = 'pt'
abbreviation_english = 'en'



language_context = 'pt'

df_original_query,_ = util_bd_pandas.read_df_original_query_and_dict_val_idg()
df_original_query = df_original_query[df_original_query['language']==language_context]
util_bd_pandas.imprime_resumo_df(df_original_query)

# deleting words: segunda
noisy_text_list = {'cod_original_query': [], 'text': []}
for index, original_query in df_original_query.iterrows():
    translated_text = translator.translate(original_query['text'],dest=abbreviation_english,src=abbreviation_portuguese).text
    back_translated_text = translator.translate(translated_text,dest=abbreviation_portuguese,src=abbreviation_english).text
    noisy_text_list['cod_original_query'].append(original_query['cod'])
    noisy_text_list['text'].append(back_translated_text)
util_bd_pandas.save_noisy_query(noisy_text_list,7,language_context)
