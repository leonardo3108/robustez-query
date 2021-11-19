""" 
Utility functions for dealing with data (files with name starting with tab_*) in dataframe

"""
import pandas as pd
import numpy as np
const_number_of_queries = 54

def read_df_original_query():
    df_original_query = pd.read_csv('data/tab_original_query.csv', sep = ';', 
        header=0, dtype= {'cod':np.int64, 'text':str, 'val_idcg10': str})
    df_original_query['val_idcg10'] = df_original_query['val_idcg10'].astype(float)        
    # print(df_original_query.dtypes)
    # print(df_original_query.head(5))
    return df_original_query 


def save_noisy_query(parm_dict_noisy_text:dict, parm_cod_noise_kind:int, parm_descr_noise_kind:str):
    """Appends data passed in tab_noise_query.csv.

    Args:
        parm_dict_noisy_text (dict): {'cod_original_query': [], 'text': []}
        parm_cod_noise_kind (int): cod of noise kind (see tab_noise_kind.csv)
        parm_descr_noise_kind (str): description of noie kind
    """
    assert 'cod_original_query' in parm_dict_noisy_text, f"Error: expected 'cod_original_query' in parm_dict_noisy_text"
    assert 'text' in parm_dict_noisy_text, f"Error: expected 'cod_original_query' in parm_dict_noisy_text"
    assert len(parm_dict_noisy_text.keys()) == 2, f"Error: expected only 2 keys in parm_dict_noisy_text"
    assert len(parm_dict_noisy_text['cod_original_query' ]) == len(parm_dict_noisy_text['text' ]), f"Error: expected same number of records in the lists in parm_dict_noisy_text"
    assert len(parm_dict_noisy_text['cod_original_query' ]) == const_number_of_queries, f"Error: expected {const_number_of_queries} queries to match number of original queries"

    # assert parm_cod_noise_kind not exists in tab_noise_kind.csv
    df_noise_kind = pd.read_csv('data/tab_noise_kind.csv', sep = ',', 
        header=0, dtype= {'cod':np.int64, 'descr':str})   
    # print(df_noise_kind.keys())
    assert parm_cod_noise_kind not in df_noise_kind['cod'], f"Error: {parm_cod_noise_kind} can not exists in tab_noise_kind.csv"



    # noisy_query: ler arquivo
    df_noisy_query = pd.read_csv('data/tab_noisy_query.csv', sep = ';', 
        header=0, dtype= {'cod_original_query':np.int64, 'cod_noise_kind':np.int64, 'text':str})   
    # noisy_query: adiciona registros no arquivo
    parm_dict_noisy_text['cod_noise_kind'] = [parm_cod_noise_kind] * const_number_of_queries     
    temp_df = pd.DataFrame.from_dict(parm_dict_noisy_text)
    #print(temp_df.head(3))
    df_noisy_query = df_noisy_query.append(temp_df, ignore_index = True, sort=True)
    # noisy_query: salva arquivo
    df_noisy_query[['cod_original_query', 'cod_noise_kind', 'text']].to_csv('data/tab_noisy_query.csv', sep = ';', index=False)   


    # noise_kind: adiciona registros no arquivo
    df_noise_kind = df_noise_kind.append({'cod':parm_cod_noise_kind, 'descr':parm_descr_noise_kind}, ignore_index = True)
    # noise_kind: salva arquivo
    df_noise_kind[['cod','descr']].to_csv('data/tab_noise_kind.csv', sep = ',', index=False)   


