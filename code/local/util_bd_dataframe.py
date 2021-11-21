""" 
Utility functions for dealing with data (files with name starting with tab_*) in dataframe

"""
import time
import pandas as pd
import numpy as np
import copy
const_number_of_queries = 54
const_cod_metric_dcg10='DCG@10'
const_cod_metric_ndcg10='nDCG@10'
const_cod_search_context_rerank = 1
const_cod_search_context_dpr = 2

def read_df_original_query():
    """Reads data from tab_original_query.csv in dataframe 
        Returns dataframe with original queries 
            and a dict dict_val_idcg10 with
                key: cod_original_query
                value: val_idcg10
    """
    df = pd.read_csv('data/tab_original_query.csv', sep = ';', 
        header=0, dtype= {'cod':np.int64, 'text':str, 'val_idcg10': str})
    df['val_idcg10'] = df['val_idcg10'].astype(float)        

    dict_val_idcg10 = {}
    for index, row in df.iterrows():
        print(index, row)
        dict_val_idcg10[row['cod']] = row['val_idcg10']
    # print(dict_val_idcg10)
    # print(df.dtypes)
    # print(df.head(5))
    # print(df.shape[0])
    return df, dict_val_idcg10

def save_df_original_query(df):
    """Reads data from tab_original_query.csv in dataframe 
    """
    assert df.shape[0] == const_number_of_queries, f"Error: expected {const_number_of_queries} queries to match number of original queries"
    df.to_csv('data/tab_original_query.csv', sep = ';', index=False) 

def read_df_noisy_query():
    """Reads data from tab_noisy_query.csv in dataframe 
    """
    df = pd.read_csv('data/tab_noisy_query.csv', sep = ';', 
        header=0, dtype= {'cod_original_query':np.int64, 'cod_noise_kind':np.int64, 'text':str})
    #print(df.dtypes)
    #print(df.head(5))
    #print(df.shape[0])
    return df 

def save_noisy_query(parm_dict_noisy_text:dict, parm_cod_noise_kind:int, parm_descr_noise_kind:str):
    """Appends data passed in tab_noise_query.csv and insert new nose_kind in tab_noise_kind.csv

    Args:
        parm_dict_noisy_text (dict): {'cod_original_query': [], 'text': []}
        parm_cod_noise_kind (int): cod of noise kind (can not exists in tab_noise_kind.csv)
        parm_descr_noise_kind (str): description of new noise kind
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


# calculated_metric
def read_df_calculated_metric():
    """Reads data from tab_calculated_metric.csv in dataframe 
    """
    df = pd.read_csv('data/tab_calculated_metric.csv', sep = ',', 
        header=0, 
        dtype= {'date_time_execution':str,'cod_metric':str,'cod_original_query':np.int64,'cod_noise_kind':np.int64,'cod_search_context':np.int64,'value':str})
    if df.shape[0]>0:
        df['value'] = df['value'].astype(float)        
    #print(df.dtypes)
    #print(df.head(5))
    #print(df.shape[0])
    return df 


def save_calculated_metric(dict_val:dict, cod_search_context:int, cod_noise_kind:int):
    print(f"saving calculated metric cod_search_context?{cod_search_context}, cod_noise_kind:{cod_noise_kind}")
    assert 'cod_original_query' in dict_val.keys(), f"Parameter dict_val.keys without cod_original_query"
    assert 'dcg10' in dict_val.keys(), f"Parameter dict_val.keys without dcg10"
    assert 'ndcg10' in dict_val.keys(), f"Parameter dict_val.keys without ndcg10"
    assert len(dict_val.keys())==3, f"Parameter dict_val.keys with unknown key {dict_val.keys()}"
    assert len(dict_val['dcg10' ]) == const_number_of_queries, f"Error: expected {const_number_of_queries} records to match number of original queries. Found {len(dict_val['dcg10' ])} in dcg10"
    assert len(dict_val['ndcg10' ]) == const_number_of_queries, f"Error: expected {const_number_of_queries} records to match number of original queries. Found {len(dict_val['ndcg10' ])} in ndcg10"
    assert len(dict_val['cod_original_query' ]) == const_number_of_queries, f"Error: expected {const_number_of_queries} records to match number of original queries. Found {len(dict_val['cod_original_query' ])} in cod_original_query"

    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    df_calculated_metric =  read_df_calculated_metric()
    save_dict_val = {}
    save_dict_val['cod_original_query'] = dict_val['cod_original_query']
    save_dict_val['date_time_execution'] = [current_time] * const_number_of_queries    
    save_dict_val['cod_search_context'] = [cod_search_context] * const_number_of_queries    
    save_dict_val['cod_noise_kind'] = [cod_noise_kind] * const_number_of_queries    


    save_dict_val['value'] = dict_val['dcg10']
    save_dict_val['cod_metric'] = [const_cod_metric_dcg10] * const_number_of_queries
    temp_df = pd.DataFrame.from_dict(save_dict_val)    
    # print('dcg10', temp_df.head(5))
    df_calculated_metric = df_calculated_metric.append(temp_df, ignore_index = True, sort=True)


    save_dict_val['value'] = dict_val['ndcg10']
    save_dict_val['cod_metric'] = [const_cod_metric_ndcg10] * const_number_of_queries
    temp_df = pd.DataFrame.from_dict(save_dict_val)    
    # print('dcg10', temp_df.head(5))
    df_calculated_metric = df_calculated_metric.append(temp_df, ignore_index = True, sort=True)


    # noisy_query: salva arquivo
    df_calculated_metric[['date_time_execution','cod_metric','cod_original_query','cod_noise_kind','cod_search_context','value']].to_csv('data/tab_calculated_metric.csv', sep = ',', index=False)   

#date_time_execution,cod_metric,cod_original_query,cod_noise_kind,cod_search_context,value
# save_calculated_metric(cod_search_context, cod_metric, valores)

