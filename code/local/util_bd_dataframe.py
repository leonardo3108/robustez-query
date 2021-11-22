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
const_cod_search_context_rerank_trec20 = 1
const_cod_search_context_dpr_trec20_judment = 2
const_cod_search_context_bm25_trec20 = 3
const_cod_search_context_bm25_trec20_judment = 4


def imprime_resumo_df(df):
    print(f"keys: {df.keys()}")
    print(f"dtypes: {df.dtypes}")
    print(f"head: {df.head}(5)")
    print(f"shape: {df.shape}[0]")



def load_judment()->dict:
    """
        Gets data from data/originals/2020qrels-pass.txt 
            (got from https://trec.nist.gov/data/deep/2020qrels-pass.txt)

        Returns 2 dicts:
            dict_judment:
                key: tuple formed by (query_nr, passage_id)
                value: relevance registered for the tuple
            dict_scale_relevance:
                key: relevance (number between 0 and 3)
                value: label associated
    Obs.:
        **Passages** were judged on a four-point scale of:
        * Not Relevant (0), 
        * Related (1), 
        * Highly Relevant (2), and 
        * Perfect (3), 

        where 'Related' is actually NOT Relevant---it means that the passage was on the same general topic, but did not answer the question. 

        Thus, for Passage Ranking task runs (only), to compute evaluation measures that use binary relevance judgments using 
        trec_eval, you either need to use 
        trec_eval's -l option [trec_eval -l 2 qrelsfile runfile]
        or modify the qrels file to change all 1 judgments to 0.
        

    """
    scale = {3:'perfectly relevant', 2:'highly relevant', 1:'related', 0:'Irrelevant'}
    judment = {}
    for i, line in enumerate(open('data/originals/2020qrels-pass.txt')):
        query_nr, _, pid, eval = line.rstrip().split()
        query_nr = int(query_nr)
        judment[(query_nr, pid)] = int(eval)

    print(f"\nLoaded len: {len(judment)} judments; judment[0] {list(judment)[0], judment[list(judment)[0]], scale[judment[list(judment)[0]]]}")
    assert len(judment)==11386, f" len(judment) {len(judment)} was expected to be 11386 as it is in https://trec.nist.gov/data/deep/2020qrels-pass.txt"
    return judment, scale


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
        dict_val_idcg10[row['cod']] = row['val_idcg10']
    # print(dict_val_idcg10)
    #imprime_resumo_df(df)
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
    #imprime_resumo_df(df)
    return df 

def read_df_noise_kind():
    """Reads data from tab_noise_kind.csv in dataframe 
    """
    df = pd.read_csv('data/tab_noise_kind.csv', sep = ',', 
        header=0, dtype= {'cod':np.int64, 'descr':str})   
    # imprime_resumo_df(df)
    return df

def read_df_search_context():
    """Reads data from tab_search_context.csv in dataframe 
    """
    df = pd.read_csv('data/tab_search_context.csv', sep = ',', 
        header=0, dtype= {'cod':np.int64,'descr_ranking_technique':str,'descr_data_description':str,'record_count':np.int64})   
    # imprime_resumo_df(df)
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
    df_noise_kind = read_df_noise_kind()
    # print(df_noise_kind.keys())
    assert parm_cod_noise_kind not in list(df_noise_kind['cod']), f"Error: {parm_cod_noise_kind} can not exists in tab_noise_kind.csv"



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
        dtype= {'date_time_execution':str,'cod_metric':str,'cod_original_query':np.int64,'cod_noise_kind':np.int64,'cod_search_context':np.int64,'value':str, 'qtd_judment_assumed_zero_relevance':np.int64})
    if df.shape[0]>0:
        df['value'] = df['value'].astype(float)        
    # imprime_resumo_df(df)
    return df 

def read_df_calculated_metric_with_label():
    """Reads data from tab_calculated_metric.csv in dataframe 
    """
    df = pd.read_csv('data/tab_calculated_metric.csv', sep = ',', 
        header=0, 
        dtype= {'date_time_execution':str,'cod_metric':str,'cod_original_query':np.int64,'cod_noise_kind':np.int64,'cod_search_context':np.int64,'value':str, 'qtd_judment_assumed_zero_relevance':np.int64})
    if df.shape[0]>0:
        df['value'] = df['value'].astype(float)        
    df_noise_kind = read_df_noise_kind()
    df = pd.merge(df, df_noise_kind, left_on='cod_noise_kind', right_on='cod',suffixes=(None,'_noise_kind'))
    df_search_context = read_df_search_context()
    df = pd.merge(df, df_search_context, left_on='cod_search_context', right_on='cod',suffixes=(None,'_search_context'))
    df['search_context'] = df['descr_data_description'] + ' - ' + df['descr_ranking_technique']
    df = df.rename(columns={"descr": "noise_kind", "qtd_judment_assumed_zero_relevance": "qtd_judment_assumed", "record_count": "base_record_count"}, errors="raise")
    df = df.drop(['cod_search_context', 'cod', 'cod_search_context', 'descr_ranking_technique', 'descr_data_description', 'cod_noise_kind'], axis = 1)
    return df

def save_calculated_metric(dict_val:dict, cod_search_context:int, cod_noise_kind:int):
    print(f"saving calculated metric cod_search_context?{cod_search_context}, cod_noise_kind:{cod_noise_kind}")
    assert 'cod_original_query' in dict_val.keys(), f"Parameter dict_val.keys without cod_original_query"
    assert 'dcg10' in dict_val.keys(), f"Parameter dict_val.keys without dcg10"
    assert 'ndcg10' in dict_val.keys(), f"Parameter dict_val.keys without ndcg10"
    assert 'qtd_judment_assumed_zero_relevance' in dict_val.keys(), f"Parameter dict_val.keys without qtd_judment_assumed_zero_relevance"
    assert len(dict_val.keys())==4, f"Parameter dict_val.keys with unknown key {dict_val.keys()}"
    assert len(dict_val['qtd_judment_assumed_zero_relevance' ]) == const_number_of_queries, f"Error: expected {const_number_of_queries} records to match number of original queries. Found {len(dict_val['qtd_judment_assumed_zero_relevance' ])} in qtd_judment_assumed_zero_relevance"
    assert len(dict_val['dcg10' ]) == const_number_of_queries, f"Error: expected {const_number_of_queries} records to match number of original queries. Found {len(dict_val['dcg10' ])} in dcg10"
    assert len(dict_val['ndcg10' ]) == const_number_of_queries, f"Error: expected {const_number_of_queries} records to match number of original queries. Found {len(dict_val['ndcg10' ])} in ndcg10"
    assert len(dict_val['cod_original_query' ]) == const_number_of_queries, f"Error: expected {const_number_of_queries} records to match number of original queries. Found {len(dict_val['cod_original_query' ])} in cod_original_query"


    # print(df_noise_kind.keys())
    df_noise_kind = read_df_noise_kind()
    assert cod_noise_kind in list(df_noise_kind['cod']), f"Error: {parm_cod_noise_kind} must exists in tab_noise_kind.csv"


    # assert cod_search_context not exists in tab_noise_kind.csv
    df_search_context = read_df_search_context()
    assert cod_search_context in list(df_search_context['cod']), f"Error: {cod_search_context} must exists in tab_search_context.csv"


    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    df_calculated_metric =  read_df_calculated_metric()
    save_dict_val = {}
    save_dict_val['cod_original_query'] = dict_val['cod_original_query']
    save_dict_val['qtd_judment_assumed_zero_relevance'] = dict_val['qtd_judment_assumed_zero_relevance']


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
    df_calculated_metric[['date_time_execution','cod_metric','cod_original_query','cod_noise_kind','cod_search_context','value','qtd_judment_assumed_zero_relevance']].to_csv('data/tab_calculated_metric.csv', sep = ',', index=False)   


