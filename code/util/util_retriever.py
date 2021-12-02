from haystack.retriever import ElasticsearchRetriever
from haystack.retriever.dense import DensePassageRetriever

def init_retriever_es_bm25(document_store):
    retriever = ElasticsearchRetriever(document_store)
    return retriever


def init_retriever_es_dpr(document_store, parm_language:str):
    assert parm_language in ['en','pt'], f"parm_language: {parm_language} is not valid: in ['en','pt']"

    if parm_language == 'pt':
        # experimentar também com voidful/dpr-question_encoder-bert-base-multilingual 
        query_embedding_model = 'castorini/mdpr-question-nq'
        passage_embedding_model = 'castorini/mdpr-passage-nq'
    elif parm_language == 'en':
        query_embedding_model='facebook/dpr-question_encoder-single-nq-base',
        passage_embedding_model='facebook/dpr-ctx_encoder-single-nq-base',

    retriever = DensePassageRetriever(
    document_store=document_store,
    query_embedding_model=query_embedding_model,
    passage_embedding_model=passage_embedding_model,
    # use_gpu=True, 
    use_gpu=False,
    embed_title=True
    )
    return retriever
